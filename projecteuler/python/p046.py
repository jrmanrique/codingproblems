from math import sqrt

from euler.mathtools import isprime, sieve


def iscounter(num):
    for p in sieve(num):
        for s in range(1, int(sqrt(num)) + 1):
            if p + 2 * pow(s, 2) == num:
                return (p, s)
    return None


def main():
    i = 3
    while isprime(i) or iscounter(i):
        i += 2
    print(i)


if __name__ == '__main__':
    main()
