# https://projecteuler.net/problem=25

from euler.mathtools import fibonacci
from euler.helpers import lend


def main():
    i = 1
    while lend(fibonacci(i)) < 1000:
        i += 1
    print(i)


if __name__ == '__main__':
    main()
