# Arbitrage

from collections import deque
from functools import reduce
from operator import mul


def load_file(file):
    with open(file) as f:
        data = f.read()
    return data


def load_input():
    inp = ''
    while True:
        try:
            line = input()
        except EOFError:
            break
        else:
            inp += line + '\n'
    return inp


def parse_input(string):
    def parse_table(strseq):
        matrix = [[float(num) for num in line.split()] for line in strseq]
        for r, row in enumerate(matrix):
            row.insert(r, 1.)
        return matrix


    inp = string.splitlines()

    cases = []
    while inp:
        dims = int(inp.pop(0))
        cases.append(parse_table(inp[:dims]))
        inp = inp[dims:]

    return cases


def convert(table, seq):
    return reduce(mul, [table[seq[i]][seq[i + 1]] for i, _ in enumerate(seq[:-1])])


def find_arbitrage(table, starting=0):
    denoms = set([d for d, _ in enumerate(table)])
    stack = deque([[starting, starting]])
    best = ([], 1)
    while stack:
        path = stack.pop()
        if len(path) >= len(denoms):
            continue
        for child in denoms - set([path[-2]]):
            new = path[:-1] + [child] + path[-1:]
            cash = convert(table, new)
            if cash >= best[1]:
                best = (new, cash)
            stack.append(new)
    if best[0]:
        return [i + 1 for i in best[0]]
    return None


def main():
    inp = load_input()
    cases = parse_input(inp)

    for case in cases:
        sol = find_arbitrage(case)
        print(' '.join([str(d) for d in sol]) if sol else 'no arbitrage sequence exists')


if __name__ == '__main__':
    main()
