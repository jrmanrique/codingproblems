# https://www.reddit.com/r/dailyprogrammer/comments/67q3s6/20170426_challenge_312_intermediate_next_largest/

from itertools import permutations as ps


def get_next(num):
    perms = sorted(set(map(lambda x: int(''.join(x)), ps(str(num)))))
    return perms[perms.index(num) + 1]


def main():
    inp = [
        1234,
        1243,
        234765,
        19000,
    ]

    for i in inp:
        print('{} => {}'.format(i, get_next(i)))


if __name__ == '__main__':
    main()
