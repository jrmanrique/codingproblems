# https://projecteuler.net/problem=5

from euler.mathtools import lcm


def main():
    maxima = 20
    numbers = [i for i in range(1, maxima + 1)]
    print(lcm(numbers))


if __name__ == '__main__':
    main()
