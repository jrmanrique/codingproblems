"""Given this matrix, a start coordinate, and an end coordinate,
return the minimum number of steps required to reach the end
coordinate from the start. If there is no possible path, then return
null. You can move up, left, down, and right. You cannot move through
walls. You cannot wrap around the edges of the board.

For example, given the following board:

[[f, f, f, f],
[t, t, f, t],
[f, f, f, f],
[f, f, f, f]]
and start = (3, 0) (bottom left) and end = (0, 0) (top left), the
minimum number of steps required to reach the end is 7, since we would
need to go through (1, 2) because there is a wall everywhere else on
the second row.
"""

class Maze:
    def __init__(self, board):
        self.board = board
        self.width = len(board[0])
        self.height = len(board)

    @property
    def valid_tiles(self):
        return [(r, c) for r, row in enumerate(self.board) for c, cell in enumerate(row) if not cell
        ]

    @classmethod
    def generate_board(cls, width, height, prob=0.2):
        from random import random

        matrix = [[(random() <= prob) for _ in range(width)] for _ in range(height)]

        return Maze(matrix)

    def _get_adjacent(self, r, c):
        ADJACENTS = {
            'U': (r - 1, c),
            'D': (r + 1, c),
            'L': (r, c - 1),
            'R': (r, c + 1),
        }
        return [(r, c) for r, c in ADJACENTS.values() if (
            0 <= r <= self.height and
            0 <= c <= self.width and
            (r, c) in self.valid_tiles
        )]

    def breadth_first(self, start, end):
        from collections import deque

        queue = deque([[start]])
        while queue:
            path = queue.popleft()
            tail = path[-1]
            if tail == end:
                return path
            for neighbor in self._get_adjacent(*tail):
                queue.append(path + [neighbor])
        return []


def main():
    from pprint import pprint
    from random import sample

    m = Maze.generate_board(5, 5)
    pprint(m.board)

    start, end = sample(m.valid_tiles, 2)
    print(start, end)
    print(m.breadth_first(start, end))


if __name__ == '__main__':
    main()
