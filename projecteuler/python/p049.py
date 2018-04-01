# https://projecteuler.net/problem=49

from itertools import combinations

from euler.mathtools import isprime, permute


def extend_set(setx, seq):
    for item in seq:
        setx.add(item)
    return setx


def hassamedist(seq):
    seq = sorted(seq)
    dists = []
    for i in range(len(seq) - 1):
        dists.append(seq[i + 1] - seq[i])
    return dists[:-1] == dists[1:]


def main():
    perms = set()
    sols = []
    for n in range(1002, 9011):
        perms = set(filter(isprime, filter(lambda x: x >= 1000, permute(n))))
        combs = set(combinations(perms, 3))

        for comb in combs:
            if hassamedist(comb) and comb not in sols:
                sols.append(comb)

    print(sols)
    print([''.join(map(str, s)) for s in sols])


if __name__ == '__main__':
    main()
