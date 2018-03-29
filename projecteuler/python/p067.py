# https://projecteuler.net/problem=67

from copy import deepcopy


def main():
    with open('inputs/p067.in') as f:
        inp = f.read()

    inp = [list(map(int, line.split())) for line in inp.splitlines()]
    width = len(inp[-1])

    grid = deepcopy(inp)
    for row in grid:
        while len(row) < width:
            row.append(-1)

    def merge(seqa, seqb):
        new = []
        for ai, a in enumerate(seqa):
            if a > 0:
                new.append(a + max(seqb[ai:ai + 2]))
            else:
                new.append(-1)
        return new

    while len(grid) > 1:
        b = grid.pop()
        a = grid.pop()
        grid.append(merge(a, b))

    print(grid[0][0])


if __name__ == '__main__':
    main()
