# https://projecteuler.net/problem=87

from itertools import product

from euler.mathtools import sieve


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
