# https://projecteuler.net/problem=2

from euler.mathtools import fibonacci


def main():
    maxima = 4 * 10 ** 6

    fibs = [0]
    i = 1
    while fibs[-1] < maxima:
        fibs.append(fibonacci(i))
        i += 1

    fibs = fibs[:-1]

    sigma = sum([f for f in fibs if f % 2 == 0])
    print(sigma)


if __name__ == '__main__':
    main()
