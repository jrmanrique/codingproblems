# https://projecteuler.net/problem=69

from euler.mathtools import sieve


def main():
    primes = sieve(10 ** 6)

    large = 1
    i = 0
    while large < 10 ** 6:
        large *= primes[i]
        i += 1
    print(large // primes[i-1])


if __name__ == '__main__':
    main()
