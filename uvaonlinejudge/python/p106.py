# Fermat vs. Pythagoras

from math import sqrt


def get_relprimes(n):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    return [k for k in range(1, n) if gcd(n, k) == 1]


def count(limit, coprimehash):
    hashtable = {k: False for k in range(1, limit + 1)}
    primitives = 0
    for m in range(2, int(sqrt(limit)) + 1):
        if m not in coprimehash:
            coprimehash[m] = get_relprimes(m)
        for n in coprimehash[m]:
            if n <= int(sqrt(limit - m ** 2)) and (m % 2) ^ (n % 2):
                primitives += 1
                for k in range(1, limit):
                    a = k * (m ** 2 - n ** 2)
                    b = k * (2 * m * n)
                    c = k * (m ** 2 + n ** 2)
                    for x in (a, b, c):
                        if x > limit:
                            break
                    else:
                        for x in (a, b, c):
                            hashtable[x] = True
                        continue
                    break
    return primitives, limit - sum(hashtable.values())


def main():
    coprimehash = {}
    while True:
        try:
            limit = int(input())
        except EOFError:
            break
        else:
            print('{} {}'.format(*count(limit, coprimehash)))


if __name__ == '__main__':
    main()
