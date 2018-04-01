# https://projecteuler.net/problem=99

from math import log

from euler.helpers import load_file


def logpower(base, exp):
    return exp * log(base)


def main():
    inp = load_file('inputs/p099.in')
    inp = [tuple(map(int, line.split(','))) for line in inp.splitlines()]

    best = (0, 0)
    for i, (base, exp) in enumerate(inp):
        num = logpower(base, exp)
        if num > best[1]:
            best = (i + 1, num)
    print(best[0])


if __name__ == '__main__':
    main()
