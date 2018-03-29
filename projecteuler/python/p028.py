# https://projecteuler.net/problem=28

def spiral(width):
    matrix = [[0] * width for _ in range(width)]
    moves = {
        'R': (0, 1),
        'D': (1, 0),
        'L': (0, -1),
        'U': (-1, 0),
    }
    actions = ['R', 'D', 'L', 'U']
    x, y = width // 2, width // 2
    j = 0
    for i in range(1, width ** 2 + 1):
        matrix[x][y] = i
        dx, dy = moves[actions[j % 4]]
        nx, ny = x + dx, y + dy
        if matrix[nx][ny] == 0:
            j += 1
        else:
            dx, dy = moves[actions[(j - 1) % 4]]
            nx, ny = x + dx, y + dy
        x, y = nx, ny
    return matrix


def sum_diagonals(matrix):
    w = len(matrix)

    diag1 = []
    diag2 = []
    for i in range(w):
        diag1.append(matrix[i][i])
        diag2.append(matrix[i][w - i - 1])
    return sum(diag1) + sum(diag2) - 1


def main():
    print(sum_diagonals(spiral(1001)))


if __name__ == '__main__':
    main()
