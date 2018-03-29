# https://projecteuler.net/problem=26

from math import sqrt


def get_relprimes(n):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    return [k for k in range(1, n) if gcd(n, k) == 1]


def phif(n):
    return len(get_relprimes(n))


def iscoprime(num, root):
    return pow(root, phif(num)) % num == 1


def get_coprimes(maxnum, root):
    return [n for n in range(1, maxnum) if iscoprime(n, root)]


def proper_divisor(num):
    yield 1

    largest = int(sqrt(num))
    if largest ** 2 == num:
        yield largest
    else:
        largest += 1

    for div in range(2, largest):
        n, r = divmod(num, div)
        if r == 0:
            yield div
            yield n


def main():
    limit = 1000

    best = (0, 0)
    for n in get_coprimes(limit, 10):
        p = phif(n)

        factors = sorted(proper_divisor(p)) + [p]
        i = 1
        while pow(10, factors[i]) % n != 1:
            i += 1
        k = factors[i]

        if k > best[1]:
            best = (n, k)

    print(best)


if __name__ == '__main__':
    main()
