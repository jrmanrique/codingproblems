import sys

from math import floor


def day_1():
    def _calc_fuel(mass: int) -> int:
        t_fuel = 0
        while True:
            mass = floor(mass / 3) - 2
            if mass > 0:
                t_fuel += mass
            else:
                break
        return t_fuel

    masses = [int(i) for i in sys.stdin.read().split('\n') if i]
    return sum([_calc_fuel(mass) for mass in masses])


if __name__ == "__main__":
    print('[OUT]', day_1())
