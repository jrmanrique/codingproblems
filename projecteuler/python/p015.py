# https://projecteuler.net/problem=15

from math import factorial


def dfs(width, start=(0, 0), goal=None):
    def get_next(coord, edge):
        x, y = coord
        ACTIONS = {
            'R': (x + 1, y),
            'D': (x, y + 1),
        }

        moves = []
        for (nx, ny) in ACTIONS.values():
            if 0 <= nx <= edge and 0 <= ny <= edge:
                moves.append((nx, ny))
        return moves


    if goal is None:
        goal = (width, width)

    solutions = []
    stack = [[[start], get_next(start, width)]]
    while stack:
        path, avail = stack.pop()
        if path[-1] == goal:
            solutions.append(path)
            continue
        for move in avail:
            stack.append([path + [move], get_next(move, width)])
    return solutions


def main():
    width = 20
    # paths = dfs(width)
    print(factorial(width * 2) / factorial(width) / factorial(width))


if __name__ == '__main__':
    main()
