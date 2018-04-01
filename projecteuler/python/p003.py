# https://projecteuler.net/problem=3

from euler.mathtools import get_prime_factors


def main():
    num = 600851475143
    primes = get_prime_factors(num)
    print(primes)
    print('MAX:', max(primes))


if __name__ == '__main__':
    main()
