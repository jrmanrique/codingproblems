# https://www.reddit.com/r/dailyprogrammer/comments/84f35x/20180314_challenge_354_intermediate_integer/
# TODO: Status: Unsolved.

from math import ceil, sqrt


def get_factors(num, primes=None):
    from functools import reduce
    from itertools import combinations_with_replacement
    from operator import mul

    if primes:
        factors = set([reduce(mul, factor) for factor in map(set, combinations_with_replacement(primes, len(primes)))])
        factors = list(filter(lambda x: x <= sqrt(num), factors))
        return [(i, num // i) for i in factors]
    return [(i, num // i) for i in range(1, ceil(sqrt(num))) if num % i == 0]


def get_prime_factors(num):
    primes = []
    i = 2
    while i ** 2 <= num:
        if num % i:
            i += 1
        else:
            num //= i
            primes.append(i)
    primes.append(num)
    return primes


def get_complexities(num):
    def gcpf(num):
        return sum(get_prime_factors(num))
    def gcfa(num):
        pairs = get_factors(num, get_prime_factors(num))
        if num == 1:
            return 1
        elif pairs:
            return min([gcpf(pair[0]) + gcpf(pair[1]) for pair in pairs])
        return num
    if num == 1:
        return gcfa(num)
    return min([gcfa(num)] + [gcfa(num - i) + i for i in range(num)])


def main():
    cases = [i for i in range(1, 100 + 1)]
    counter = 0
    for _, case in enumerate(cases):
        test = get_complexities(case)
        print('{} => {}'.format(case, test))
        counter += test
    print('Inclusive sum:', counter)


if __name__ == '__main__':
    main()
