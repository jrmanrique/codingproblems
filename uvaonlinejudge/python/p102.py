# Ecological Bin Packing

from itertools import permutations



def checker(bins, config):
    movements = sum([sum(b) - b[k] for b, k in zip(bins, config)])
    return ''.join(['BGC'[i] for i in config]), movements


def move(bins):
    solutions = {}
    for perm in permutations([0, 1, 2]):
        config, score = checker(bins, perm)
        if score not in solutions:
            solutions[score] = [config]
        else:
            solutions[score] += [config]
    best = min(solutions)
    return sorted(solutions[best])[0], best


def main():
    while True:
        try:
            inp = input()
        except EOFError:
            break
        else:
            inp = inp.split()
            bins = [[int(d) for d in inp[i * 3:(i + 1) * 3]] for i in range(3)]
            print('{} {}'.format(*move(bins)))


if __name__ == '__main__':
    main()
