# https://www.reddit.com/r/dailyprogrammer/comments/82pt3h/20180307_challenge_353_intermediate/
# TODO: Bonus Status: Unsolved.

def input_case():
    n = int(input())
    m = input()
    return list(map(int, m.split()))[:n]


def flip(lst, idx):
    return lst[:idx + 1][::-1] + lst[idx + 1:]


def pancake(lst):
    def stringify(lst):
        return '-'.join(list(map(str, lst)))

    goal = sorted(lst, reverse=True)
    moves = [stringify(lst)]
    i = 0
    while stringify(lst) != stringify(reversed(goal)):
        j = len(lst) - i - 1
        idx = lst.index(goal[i], 0, j + 1)
        if goal[i] != lst[j]:
            if goal[i] != lst[0]:
                lst = flip(lst, idx)
                moves.append(stringify(lst))
            lst = flip(lst, j)
            moves.append(stringify(lst))
        i += 1
    return moves


def main():
    case = input_case()
    moves = pancake(case)
    print('{} flips: {}'.format(len(moves) - 1, ' -> '.join(moves)))


if __name__ == '__main__':
    main()
