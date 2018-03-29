# https://projecteuler.net/problem=60

import pickle

from itertools import combinations as cmb
from math import sqrt


def isprime(num):
    for factor in range(2, int(sqrt(num) + 1)):
        if num % factor == 0:
            return False
    return True


def isspecial(seq):
    def _concat(a, b):
        return int(str(a) + str(b))

    def _helper(a, b):
        return isprime(_concat(a, b)) and isprime(_concat(b, a))

    for p in cmb(seq, 2):
        if not _helper(*p):
            return False
    return True


def main():
    limit = 2 * 10 ** 4

    primes = []
    for n in range(2, limit):
        if isprime(n):
            primes.append(n)

    print(primes[-10:])
    print('LENGTH:', len(primes))

    concat = lambda a, b: int(str(a) + str(b))

    def _isprime(num):
        if num > limit:
            return isprime(num)
        return num in primes

    for comb in cmb(primes, 5):
        for pair in cmb(comb, 2):
            a, b = pair
            if not(_isprime(concat(a, b)) and _isprime(concat(b, a))):
                break
        else:
            print(comb)


def test():
    def make_hashtable(primes):
        table = {}
        for i, a in enumerate(primes):
        # for a in primes:
            table[a] = set()
            for b in primes[i + 1:]:
            # for b in filter(lambda x: x > a, primes):
                if isspecial([a, b]):
                    table[a].add(b)
        return table


    limit = 2 * 10 ** 4

    def sieve(num):
        sieve = {n: True for n in range(2, num + 1)}
        for n in range(2, num + 1):
            if sieve[n]:
                for a in range(2, limit // n + 1):
                    sieve[n * a] = False
        return [k for k, v in sieve.items() if v]

    primes = sieve(limit)
    print('Sieved!')

    level2 = [(a, b) for a in primes for b in filter(lambda x: x > a, primes) if isspecial([a, b])]
    print('Level 2! Pairs:', len(level2))

    level3 = [(a, b, c) for a, b in level2 for c in filter(lambda x: x > b, primes) if isspecial([a, b, c])]
    print('Level 3! Pairs:', len(level3))

    level3 = pickle.load(open('level3.pkl', 'rb'))
    print('Level 3! Pairs:', len(level3))

    level4 = [(a, b, c, d) for a, b, c in level3 for d in filter(lambda x: x > c, primes) if isspecial([a, b, c, d])]
    print(level4, len(level4))

    level5 = [(a, b, c, d, e) for a, b, c, d in level4 for e in filter(lambda x: x > d, primes) if isspecial([a, b, c, d, e])]
    print(level5, len(level5))


if __name__ == '__main__':
    # main()
    test()
