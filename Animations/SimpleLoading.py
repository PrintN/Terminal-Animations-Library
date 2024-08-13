import time
import sys

symbols = ['/', '-', '\\', '|']
delay = 0.1
def play_simple_loading():
    while True:
        for symbol in symbols:
            sys.stdout.write('\r' + symbol)
            sys.stdout.flush()
            time.sleep(delay)

play_simple_loading()