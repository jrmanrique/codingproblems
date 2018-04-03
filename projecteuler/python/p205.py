# https://projecteuler.net/problem=205

import random as rd


def main():
    trials = 10 ** 8
    counter = 0
    for _ in range(trials):
        p = 0
        for _ in range(9):
            p += rd.randint(1, 4)
        c = 0
        for _ in range(6):
            c += rd.randint(1, 6)
        if p > c:
            counter += 1
    print(counter / trials)


if __name__ == '__main__':
    main()
