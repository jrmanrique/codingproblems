# https://projecteuler.net/problem=74

from functools import lru_cache
from math import factorial


@lru_cache(maxsize=None)
def get_next(num):
    return sum([factorial(int(d)) for d in str(num)])


def get_chain(num):
    chain = [num]
    while True:
        new = get_next(chain[-1])
        if new not in chain:
            chain.append(new)
        else:
            return chain


def main():
    counter = 0
    for n in range(1, 10 ** 6 + 1):
        if len(get_chain(n)) == 60:
            counter += 1
    print(counter)


if __name__ == '__main__':
    main()
