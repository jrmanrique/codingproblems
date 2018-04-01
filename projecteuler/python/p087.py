# https://projecteuler.net/problem=87

from itertools import product


def sieve(limit):
    sieve = {n: True for n in range(2, limit + 1)}
    for n in range(2, limit + 1):
        if sieve[n]:
            for a in range(2, limit // n + 1):
                sieve[n * a] = False
    return [k for k, v in sieve.items() if v]


def main():
    limit = 50 * 10 ** 6
    powers = {2: {}, 3: {}, 4: {}}
    seen = set()
    for a, b, c in product(sieve(7072), sieve(369), sieve(85)):
        if a not in powers[2]:
            powers[2][a] = a ** 2
        if b not in powers[3]:
            powers[3][b] = b ** 3
        if c not in powers[4]:
            powers[4][c] = c ** 4
        num = powers[2][a] + powers[3][b] + powers[4][c]
        if num > limit:
            continue
        if num not in seen:
            seen.add(num)
    print(len(seen))


if __name__ == '__main__':
    main()
