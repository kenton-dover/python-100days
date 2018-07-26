from itertools import cycle
import random
from time import sleep

LIGHTCOLORS = ["Green", "Yellow", "Red"]


def trafficLightLoop():
    light = cycle(LIGHTCOLORS)
    while True:
        sleep(1)


def main():
    trafficLightLoop()


if __name__ == '__main__':
    main()
