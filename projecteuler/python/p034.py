# https://projecteuler.net/problem=34

from math import factorial

from euler.typetools import get_digits


def main():
    totals = 0
    for i in range(10, 10 ** 6):
        if sum(map(factorial, get_digits(i))) == i:
            totals += i
            print(i, totals)


if __name__ == '__main__':
    main()
