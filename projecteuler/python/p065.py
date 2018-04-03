# https://projecteuler.net/problem=65

from euler.helpers import deepflatten


def main():
    limit = 100
    a = deepflatten([0] + [[1, 2 * i, 1] for i in range(1, limit // 3 + 2)])

    x = 2
    y = 3
    for k in range(3, limit + 1):
        c = a[k - 1] * y + x
        x, y = y, c

    print(c)
    print('ANSWER:', sum([int(d) for d in str(c)]))


if __name__ == '__main__':
    main()
