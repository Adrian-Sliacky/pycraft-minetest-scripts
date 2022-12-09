import colorama
import sys
import time
import math


class ProgressBar:
    def __init__(self, total, color=colorama.Fore.YELLOW):
        self.total = total
        self.color = color
        self.start = None
        self.running = True
        self.progress = 0

    def start_pbar(self):
        self.start = time.time()

    def progress_bar(self, text='Building... '):
        if not self.progress == 0:
            eta = (self.total - self.progress) * ((time.time() - self.start) / self.progress)
        else:
            eta = '♾'
        percent = 100 * (self.progress / float(self.total))
        bar = '█' * int(percent) + '-' * (100 - int(percent))
        sys.stdout.write(
            self.color + f'\rBuilding... |{bar}| {percent:.2f}% ETA: {(math.trunc(eta)) if type(eta) == float else eta}s      ' + '\r')
        if self.progress == self.total:
            sys.stdout.write(colorama.Fore.GREEN + f'\r{text}|{bar}| {percent:.2f}%         ' + '\r')

    def set_progress(self, progress):
        self.progress = progress

    def main(self):
        while self.running:
            self.progress_bar()
            time.sleep(.01)
        self.progress = self.total
        self.progress_bar()
