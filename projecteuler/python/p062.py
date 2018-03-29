# https://projecteuler.net/problem=62

from itertools import permutations


def permute(num):
    return set(int(''.join(p)) for p in permutations(str(num)))


def cbrt(num):
    return pow(num, 1/3)


def isperfect(num):
    return round(cbrt(num)) ** 3 == num


def largeperm(num):
    return int(''.join(sorted([d for d in str(num)], reverse=True)))


def main():
    n = 100

    found = False
    cache = {}
    while not found:
        smallperm = largeperm(n ** 3)
        if smallperm not in cache:
            cache[smallperm] = {'times': 1, 'perms': [n]}
        else:
            cache[smallperm]['times'] += 1
            cache[smallperm]['perms'] += [n]
        if cache[smallperm]['times'] == 5:
            found = True
            result = cache[smallperm]
        else:
            n += 1

    print(result['perms'])
    print('ANSWER:', min(result['perms']) ** 3)


if __name__ == '__main__':
    main()
