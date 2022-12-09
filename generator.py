import cv2
import os
import sys
import math
import numpy as np
from PIL import Image, ImageDraw, ImageFont


def to_black_and_white(file):
    original_image = cv2.imread(file)
    gray_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    (thresh, black_and_white_image) = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)
    cv2.imwrite(file, black_and_white_image)


def clean_array(s):
    ar_len_x = 0
    ar_len_y = 0
    min_x = 2147483647
    max_x = 0
    min_y = 2147483647
    max_y = 0
    for _, row in enumerate(s):
        for _2, val in enumerate(row):
            if val == 1:
                if _ < min_x:
                    min_x = _
                if _ > max_x:
                    max_x = _
                if _2 < min_y:
                    min_y = _2
                if _2 > max_y:
                    max_y = _2
            else:
                if _ > ar_len_x:
                    ar_len_x = _
                if _2 > ar_len_y:
                    ar_len_y = _2
    row_del = []
    for num in range(min_x):
        row_del.append(num)
    for num in range(max_x + 1, ar_len_x):
        row_del.append(num)
    col_del = []
    for num in range(min_y):
        col_del.append(num)
    for num in range(max_y + 1, ar_len_y):
        col_del.append(num)
    th = s
    th = np.delete(th, tuple(row_del), axis=0)
    th = np.delete(th, tuple(col_del), axis=1)
    return th


class Generator:
    def __init__(self):
        pass

    def generate(self, user_input, resolution):
        length = len(user_input)
        width = math.ceil(length * resolution)
        height = resolution * 2
        white = (255, 255, 255)

        fnt = ImageFont.truetype("fonts/helvetica.ttf", resolution)
        image1 = Image.new("RGB", (width, height), white)
        draw = ImageDraw.Draw(image1)
        draw.text((2, 0), user_input, font=fnt, fill=(0, 0, 0, 255))
        filename = "my_drawing.png"
        image1.save(filename)
        to_black_and_white(filename)
        img = cv2.imread(filename, 0)
        img_reverted = cv2.bitwise_not(img)
        new_img = img_reverted / 255.0
        os.remove(filename)
        return clean_array(new_img)
