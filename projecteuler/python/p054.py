# https://projecteuler.net/problem=54

from collections import Counter


def unpack_hand(hand):
    table = {k: v for v, k in enumerate('23456789TJQKA')}
    nums = [table[h[0]] for h in hand]
    suit = [h[1] for h in hand]
    return nums, suit


def isconsecutive(nums):
    order = ''.join([str(12)] + [str(i) for i in range(13)])
    return ''.join([str(n) for n in nums]) in order


def compute_score(hand):
    nums, suit = unpack_hand(hand)

    cnums = Counter(nums)
    csuit = Counter(suit)

    samesuit = [k for k, v in csuit.items() if v == 5]
    kind = lambda x: [k for k, v in cnums.items() if v == x]

    if isconsecutive(nums) and samesuit and 12 in nums:
        return 9 * 13
    elif isconsecutive(nums) and samesuit:
        return 8 * 13 + max(nums)
    elif kind(4):
        return 7 * 13 + max(kind(4))
    elif kind(3) and kind(2):
        return 6 * 13 + max(kind(3))
    elif samesuit:
        return 5 * 13 + max(nums)
    elif isconsecutive(nums):
        return 4 * 13 + max(nums)
    elif kind(3):
        return 3 * 13 + max(kind(3))
    elif len(kind(2)) == 2:
        return 2 * 13 + max(kind(2))
    elif kind(2):
        return 1 * 13 + max(kind(2))
    else:
        return max(nums)


def get_winner(p1, p2):
    def get_max(hand, place):
        nums, _ = unpack_hand(hand)
        return sorted(nums, reverse=True)[place]


    p1s, p2s = compute_score(p1), compute_score(p2)

    i = 0
    while p1s == p2s:
        p1s = get_max(p1, i)
        p2s = get_max(p2, i)
        i += 1

    if p1s > p2s:
        return 1, (p1s, p2s)
    else:
        return 2, (p1s, p2s)


def main():
    def parse(inp):
        inp = inp.split()
        return inp[:5], inp[5:]

    def load_file(file):
        with open(file, 'r') as f:
            data = f.read()
        return data


    # inputs = [
    #     '5H 5C 6S 7S KD 2C 3S 8S 8D TD',
    #     '5D 8C 9S JS AC 2C 5C 7D 8S QH',
    #     '2D 9C AS AH AC 3D 6D 7D TD QD',
    #     '4D 6S 9H QH QC 3D 6D 7H QD QS',
    #     '2H 2D 4C 4D 4S 3C 3D 3S 9S 9D',
    # ]

    inputs = load_file('inputs/p054.in')
    inputs = inputs.splitlines()

    winners = []
    for _, inp in enumerate(inputs):
        p1, p2 = parse(inp)
        winner, _ = get_winner(p1, p2)
        winners.append(winner)

    print(Counter(winners))


if __name__ == '__main__':
    main()
