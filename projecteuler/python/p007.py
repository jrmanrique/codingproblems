# https://projecteuler.net/problem=7

import random as rd

from math import ceil, log2, sqrt


def isprime(num):
    def get_sd(num):
        for s in range(1, ceil(log2(num - 1))):
            d, rem = divmod(num - 1, 2 ** s)
            if rem == 0 and d % 2:
                    return s, d
        return None

    def _millerrabin(num):
        if num % 2 == 0:
            return False

        s, d = get_sd(num)
        a = rd.randint(1, num - 1)
        for r in range(s):
            test = pow(a, pow(2, r) * d) % num
            if test == num - 1:
                return True
        return False

    def _bruteforce(num):
        for factor in range(2, int(sqrt(num) + 1)):
            if num % factor == 0:
                return False
        return True

    return _bruteforce(num)


def get_next_prime(num):
    while not isprime(num + 1):
        num += 1
    return num + 1


def main():
    num = 10001

    prime = 2
    for _ in range(num - 1):
        prime = get_next_prime(prime)

    print(prime)


if __name__ == '__main__':
    main()
