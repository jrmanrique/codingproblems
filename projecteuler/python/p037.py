# https://projecteuler.net/problem=37

from math import sqrt

from euler.mathtools import isprime


def truncate(num):
    num = str(num)
    truncs = set()
    for i in range(len(num)):
        truncs.add(num[i:])
        truncs.add(num[:i])
    truncs.remove('')
    return [int(t) for t in truncs]


def main():
    total = 0
    for n in range(10, 10 ** 6):
        if all([isprime(p) for p in truncate(n)]):
            total += n
            print(n, total)


if __name__ == '__main__':
    main()
