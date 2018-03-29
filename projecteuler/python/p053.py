# https://projecteuler.net/problem=53

import matplotlib.pyplot as plt

from math import factorial as fct


def ncr(n, r):
    if r > n:
        return None
    return fct(n) // (fct(r) * fct(n - r))


def main():
    counter = 0
    for n in range(1, 100 + 1):
        for r in range(1, n + 1):
            if ncr(n, r) > 10 ** 6:
                counter += 1
                print(n, r, counter)


def bonus():
    n = 100
    data = [ncr(n, i) for i in range(1, n + 1)]

    plt.style.use('ggplot')
    plt.plot(data, '.')
    plt.show()


if __name__ == '__main__':
    main()
    # bonus()
