# https://projecteuler.net/problem=41

from itertools import permutations
from math import sqrt


def isprime(num):
    if num < 0:
        return False
    for factor in range(2, int(sqrt(num) + 1)):
        if num % factor == 0:
            return False
    return True


def generate_pandigitals(length):
    digits = [i for i in range(1, length + 1)][::-1]
    return (int(''.join(map(str, p))) for p in permutations(digits))


def main():
    for l in range(9, 0, -1):
        for p in generate_pandigitals(l):
            if isprime(p):
                print(p)
                break


if __name__ == '__main__':
    main()
