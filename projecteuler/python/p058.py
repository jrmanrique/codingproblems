# https://projecteuler.net/problem=58

from math import sqrt


def isprime(num):
    for factor in range(2, int(sqrt(num) + 1)):
        if num % factor == 0:
            return False
    return True


def main():
    width = 5
    primes = 3
    num = 13
    while primes / ((width // 2) * 4 + 1) > 0.10:
        for _ in range(3):
            if isprime(num):
                primes += 1
            num += width - 1
        width += 2
        num += width - 1

    print('Spiral side length:', width)
    print('Primes on diagonal:', primes)


if __name__ == '__main__':
    main()
