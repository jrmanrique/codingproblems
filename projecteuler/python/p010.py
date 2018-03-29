# https://projecteuler.net/problem=10

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
    num = 2 * 10 ** 6

    primes = [2]
    while primes[-1] < num:
        primes.append(get_next_prime(primes[-1]))

    print(sum(primes[:-1]))


if __name__ == '__main__':
    main()
