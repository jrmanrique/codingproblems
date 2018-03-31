from itertools import permutations

# Ecological Bin Packing

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
    inputs = [
        '1 2 3 4 5 6 7 8 9',
        '5 10 5 20 10 5 10 20 10',
    ]

    for inp in inputs:
        inp = inp.split()
        bins = [[int(d) for d in inp[i * 3:(i + 1) * 3]] for i in range(3)]
        print('{} {}'.format(*move(bins)))


if __name__ == '__main__':
    main()
