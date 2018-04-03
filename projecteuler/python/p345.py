# https://projecteuler.net/problem=345

import re

from euler.helpers import deepflatten, load_file


class Matrix:
    def __init__(self, board):
        self.board = board
        self.width = len(self.board)

    def find_position(self, num):
        flat = deepflatten(self.board)
        idx = flat.index(num)
        return divmod(idx, self.width)

    def rotate(self, clockwise=True):
        matrix = self.board
        r, c = self.width

        if clockwise:
            cols = range(c)
            rows = range(r - 1, -1, -1)
        else:
            cols = range(c - 1, -1, -1)
            rows = range(r)

        return [[matrix[row][col] for row in rows] for col in cols]

    def pop(self, x, y):
        return Matrix([self.board[r][:y] + self.board[r][y + 1:] for r, _ in enumerate(self.board) if r != x])

    def __str__(self):
        return str(self.board)


def main():
    inp = load_file('inputs/p345.in').splitlines()
    inp = [list(map(int, re.sub('\s+', ' ', line).split())) for line in inp]
    m = Matrix(inp)

    # TODO: Hungarian Algorithm: https://en.wikipedia.org/wiki/Hungarian_algorithm



if __name__ == '__main__':
    main()
