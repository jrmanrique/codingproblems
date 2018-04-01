# https://projecteuler.net/problem=75

from math import sqrt
from euler.mathtools import gcf


def main():
    limit = 1500000
    result = 0
    triangles = {k: 0 for k in range(1, limit + 1)}
    for m in range(2, int(sqrt(limit / 2)) + 1):
        for n in range(1, m):
            if (n + m) % 2 and gcf([n, m]) == 1:
                a = m ** 2 + n ** 2
                b = 2 * m * n
                c = m ** 2 - n ** 2
                p = a + b + c
                while p <= limit:
                    triangles[p] += 1
                    if triangles[p] == 1:
                        result += 1
                    elif triangles[p] == 2:
                        result -= 1
                    p += a + b + c
    print(result)

if __name__ == '__main__':
    main()
