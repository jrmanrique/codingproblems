# https://projecteuler.net/problem=35

from math import sqrt


def isprime(num):
    if num < 0:
        return False
    for factor in range(2, int(sqrt(num) + 1)):
        if num % factor == 0:
            return False
    return True


def rotate(num):
    num = str(num)
    rots = []
    for i in range(len(num)):
        rots.append(num[i:] + num[:i])
    return [int(n) for n in rots]


def main():
    counter = 0
    for n in range(2, 10 ** 6):
        if all([isprime(r) for r in rotate(n)]):
            counter += 1
            print(n, counter)


if __name__ == '__main__':
    main()
