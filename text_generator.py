import subprocess
import sys
import os
import time

subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

for i in range(10):
    print('\n')
os.system('cls')
import minetest
import generator


def is_ascii(s):
    return all(ord(c) < 128 for c in s)


user_input = input('Text: ')
if user_input.strip() == '' or is_ascii(user_input) is False:
    exit()
user_resolution = input('Text resolution (minimum is 15): ')
if user_resolution == '':
    user_resolution = 15

try:
    user_resolution = int(user_resolution)
except ValueError:
    exit('invalid input')

if user_resolution < 15:
    exit('Text resolution minimum is 15')
user_vertical = True  # True by default
user_depth = 1
distance_from_player_x = 15
distance_from_player_y = 1
distance_from_player_z = -(round(user_resolution / 2))

if not is_ascii(user_input):
    exit('Your string isn\'t in ASCII!')

gen = generator.Generator()
mt = minetest.Minetest(distance_from_player_x, distance_from_player_y, distance_from_player_z, block='diamond')
gen_ar = gen.generate(user_input, user_resolution)
position_prefix = 0  # for creating multi-line printouts
for j in range(5):
    for i in range(user_resolution // 2):
        mt.block = 'diamond'
        mt.draw_from_array(gen_ar, user_depth, user_vertical, z=i)
        time.sleep(0.2)
        mt.block = 'air'
        mt.draw_from_array(gen_ar, user_depth, user_vertical, z=i)
