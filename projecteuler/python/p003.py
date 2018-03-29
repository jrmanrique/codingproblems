# https://projecteuler.net/problem=3

from math import ceil, sqrt


def get_prime_factors(num):
    def get_next_prime(num):
        for div in range(2, ceil(sqrt(num))):
            if num % div == 0:
                num = num // div
                return num, div
        return 1, num

    factors = []
    while num != 1:
        num, factor = get_next_prime(num)
        factors.append(factor)
    return factors


def main():
    num = 600851475143
    primes = get_prime_factors(num)
    print(primes)
    print('MAX:', max(primes))


if __name__ == '__main__':
    main()
