# https://projecteuler.net/problem=24

from itertools import permutations


def main():
    seq = [str(i) for i in range(10)]
    perms = sorted(map(lambda x: ''.join(x), permutations(seq)))
    print(perms[10 ** 6 - 1])


if __name__ == '__main__':
    main()
