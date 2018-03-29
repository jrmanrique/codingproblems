# https://www.reddit.com/r/dailyprogrammer/comments/3r7wxz/20151102_challenge_239_easy_a_game_of_threes/

from itertools import zip_longest as zip


def threes(num):
    def get_move(num):
        tree = {0: [0], 1: [-1, 2], 2: [1, -2]}
        if num == 2:
            return [1]
        return tree[num % 3]

    solutions = []
    stack = [([num], get_move(num), [])]
    while stack:
        path, moves, real = stack.pop()
        if path[-1] == 1:
            if sum(real) == 0:
                solutions.append(list(zip(path, real, fillvalue=0)))
                return solutions
            continue
        for move in moves:
            new = (path[-1] + move) // 3
            stack.append((path + [new], get_move(new), real + [move]))

    return solutions


def main():
    num = 18446744073709551615
    print(threes(num))


if __name__ == '__main__':
    main()
