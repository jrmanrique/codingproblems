# https://projecteuler.net/problem=81


def load_file(file):
    with open(file) as f:
        data = f.read()
    return data


def backtrack(start, goal, matrix):
    def get_moves(x, y, height, width):
        ACTIONS = {
            'U': (x - 1, y),
            'L': (x, y - 1),
        }
        moves = []
        for (nx, ny) in ACTIONS.values():
            if 0 <= nx <= height and 0 <= ny <= width:
                moves.append((nx, ny))
        return moves

    def get_best_move(matrix, moves):
        children = [(matrix[nx][ny], (nx, ny)) for (nx, ny) in moves]
        return sorted(children)[0][1]

    def get_values(path):
        return [matrix[x][y] for (x, y) in path]

    gx, gy = goal
    height, width = gx + 1, gy + 1

    path = [(gx, gy)]
    while path[-1] != start:
        ox, oy = path[-1]
        move = get_best_move(matrix, get_moves(ox, oy, height, width))
        path.append(move)

    return sum(get_values(path)), path


def djikstra(matrix):
    out = matrix
    width, height = len(matrix), len(matrix[-1])
    for r in range(height):
        for c in range(width):
            if r == 0 and c == 0:
                out[r][c] = matrix[r][c]
            elif r == 0:
                out[r][c] = matrix[r][c] + out[r][c - 1]
            elif c == 0:
                out[r][c] = matrix[r][c] + out[r - 1][c]
            else:
                out[r][c] = matrix[r][c] + min([out[r][c - 1], out[r - 1][c]])
    return out[-1][-1]


def main():
    inp = load_file('inputs/p081.in')
    inp = [list(map(int, line.split(','))) for line in inp.splitlines()]

    score = djikstra(inp)
    print(score)
    print('CORRECT ANSWER:', score == 427337)


if __name__ == '__main__':
    main()
