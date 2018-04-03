# https://projecteuler.net/problem=21

from math import sqrt

from euler.helpers import deepflatten


def get_divisors(num):
    return set(deepflatten([[i, num // i] for i in range(1, int(sqrt(num)) + 1) if num % i == 0]))


def main():
    limit = 10 ** 4
    d = lambda x: get_divisors(x) - set([x])

    amicable = set()
    cache = {}
    for a in range(1, limit + 1):
        if a not in cache:
            cache[a] = sum(d(a))
        for b in range(a + 1, limit + 1):
            if b not in cache:
                cache[b] = sum(d(b))
            if cache[a] == b and cache[b] == a:
                amicable.add(a)
                amicable.add(b)

    print(sum(amicable))


if __name__ == '__main__':
    main()
