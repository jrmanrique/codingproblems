# https://projecteuler.net/problem=12

from math import sqrt

from euler.helpers import deepflatten


def generate_nth_trinum(n):
    return sum([i for i in range(1, n + 1)])


def get_divisors(num):
    return set(deepflatten([[i, num // i] for i in range(1, int(sqrt(num)) + 1) if num % i == 0]))


def main():
    num = 500
    i = 1
    while len(get_divisors(generate_nth_trinum(i))) < num:
        i += 1
    print(i, generate_nth_trinum(i))


if __name__ == '__main__':
    main()
