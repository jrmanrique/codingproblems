# https://www.reddit.com/r/dailyprogrammer/comments/83uvey/20180312_challenge_354_easy_integer_complexity_1/

from math import ceil, sqrt


def get_cases():
    t = int(input())

    cases = []
    for _ in range(t):
        a = int(input())
        cases.append(a)

    return cases


def get_factors(num, primes=None):
    from functools import reduce
    from itertools import combinations_with_replacement
    from operator import mul

    if primes:
        primes = list(map(int, primes.split('*')))
        factors = set([reduce(mul, factor) for factor in map(set, combinations_with_replacement(primes, len(primes)))])
        return [(i, num // i) for i in factors]
    return [(i, num // i) for i in range(1, ceil(sqrt(num))) if num % i == 0]


def compute_complexity(number, primes=None):
    factors = get_factors(number, primes=primes)
    sums = [sum(factor) for factor in factors]
    minima = min(sums)
    pair = factors[sums.index(minima)]
    return minima, pair


def main():
    # cases = get_cases()
    cases = [12, 456, 4567, 12345, 1234567891011]
    for _, case in enumerate(cases):
        minima, pair = compute_complexity(case)
        print('{} => {} {}'.format(case, minima, pair))


def bonus_2():
    NUMBER = 6789101112131415161718192021
    PRIMES = '3*3*3*53*79*1667*20441*19646663*89705489'
    minima, pair = compute_complexity(NUMBER, PRIMES)
    print('{} => {} {}'.format(NUMBER, minima, pair))


if __name__ == '__main__':
    main()
    bonus_2()
