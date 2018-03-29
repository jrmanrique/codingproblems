# https://projecteuler.net/problem=37

from math import sqrt


def isprime(num):
    if num < 2:
        return False
    for factor in range(2, int(sqrt(num) + 1)):
        if num % factor == 0:
            return False
    return True


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
