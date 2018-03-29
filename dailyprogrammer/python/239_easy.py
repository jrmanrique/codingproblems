# https://www.reddit.com/r/dailyprogrammer/comments/3r7wxz/20151102_challenge_239_easy_a_game_of_threes/

def threes(num):
    moves = []
    while num != 1:
        n, rem = divmod(num, 3)
        moves.append((num, (0, -1, 1)[rem]))
        num = n + 1 if rem == 2 else n
    return moves + [(1, 0)]


def main():
    num = 929
    print(threes(num))


if __name__ == '__main__':
    main()
