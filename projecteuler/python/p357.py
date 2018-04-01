# https://projecteuler.net/problem=357

from euler.mathtools import get_divisors, sieve


def main():
    limit = 10 ** 6

    primes = set(sieve(limit))
    total = 1
    for i in range(2, limit + 1, 4):
        for d in get_divisors(i):
            if (d + i // d) not in primes:
                break
        else:
            total += i
    print(total)

if __name__ == '__main__':
    main()
