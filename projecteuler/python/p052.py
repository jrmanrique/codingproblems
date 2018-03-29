# https://projecteuler.net/problem=52

from itertools import permutations


def permute(num):
    return (int(''.join(p)) for p in permutations(str(num)))


def main():
    degree = 5
    length = 6

    solutions = set()
    start = int('10' + '1' * (degree - 2) + '0')
    start = start + (9 - start % 9)
    end = (10 ** (degree + 1) - 10) // length + 1
    for n in range(start, end, 9):
        if (length >= 5) and ('5' not in str(n)) and ('0' not in str(n)):
            continue
        print(n, len(solutions))
        perms = set(permute(n))
        if all([m in perms for m in [n * l for l in range(1, length + 1)]]):
            solutions.add(n)
            break

    print()
    print(solutions)


if __name__ == '__main__':
    main()
