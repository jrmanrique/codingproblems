# https://projecteuler.net/problem=5

from functools import reduce


def lcm(seq):
    def _gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    def _lcm(a, b):
        return (a * b) // _gcd(a, b)

    return reduce(_lcm, seq)


def main():
    maxima = 20
    numbers = [i for i in range(1, maxima + 1)]
    print(lcm(numbers))


if __name__ == '__main__':
    main()
