"""The area of a circle is defined as πr^2. Estimate π to 3 decimal
places using a Monte Carlo method.

Hint: The basic equation of a circle is x^2 + y^2 = r^2.
"""

from itertools import product


def main():
    r = 10 ** 5
    inner = 0
    total = 0
    for x, y in product(range(2 * r + 1), range(2 * r + 1)):
        if (x - r) ** 2 + (y - r) ** 2 <= r ** 2:
            inner += 1
        total += 1
    print((inner / total) * 4)


if __name__ == '__main__':
    main()
