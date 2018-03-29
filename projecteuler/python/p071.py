# https://projecteuler.net/problem=71

from fractions import Fraction as f


def main():
    limit = 8

    fractions = set()
    for d in range(2, limit):
        for n in range(1, d):
            fractions.add(f(n, d))

    # fractions = sorted(fractions)
    # print(fractions[fractions.index(f(3, 7)) - 1])

    print(int(3 / 7 * 10 ** 6) - 1)


if __name__ == '__main__':
    main()
