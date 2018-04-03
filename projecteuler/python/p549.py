from collections import Counter
from functools import lru_cache

from euler.mathtools import gcf, get_prime_factors


def s(n):
    @lru_cache()
    def _s(n):
        m = 1
        while n > 1:
            m += 1
            n = n // gcf([n, m])
        return m

    primes = [k ** v for k, v in Counter(get_prime_factors(n)).items()]
    if len(primes) == 1 and primes[0] == n:
        return _s(n)
    return max([s(p) for p in primes])


def S(n):
    total = 0
    for i in range(2, n + 1):
        total += s(i)
    return total


def main():
    print(S(10 ** 3))


if __name__ == '__main__':
    main()
