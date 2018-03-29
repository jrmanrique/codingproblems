# https://projecteuler.net/problem=33

from functools import reduce
from operator import mul


def get_digits(num):
    return [int(d) for d in str(num)]


def can_cancel(a, b):
    return any([ad for ad in get_digits(a) if ad in get_digits(b)])


def cancel(a, b):
    if can_cancel(a, b):
        ad = get_digits(a)
        bd = get_digits(b)
        for d in ad:
            if d in bd:
                ad.remove(d)
                bd.remove(d)
                a = ad[0]
                b = bd[0]
                break
    return a, b


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def main():
    solutions = []
    for a in range(10, 99 + 1):
        for b in range(a + 1, 99 + 1):
            if can_cancel(a, b):
                c, d = cancel(a, b)
                try:
                    nontrivial = a/b == c/d
                except ZeroDivisionError:
                    pass
                else:
                    if nontrivial:
                        solutions.append((a, b))

    num = reduce(mul, [i[0] for i in solutions])
    den = reduce(mul, [i[1] for i in solutions])
    print('{}/{}'.format(num // gcd(num, den), den // gcd(num, den)))


if __name__ == '__main__':
    main()
