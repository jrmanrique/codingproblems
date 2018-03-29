# https://www.reddit.com/r/dailyprogrammer/comments/576o8o/20161012_challenge_287_intermediate_mathagrams/

from itertools import permutations as ps


def mathagram(problem):
    nums = set([i for i in ''.join(problem.split()[::2]) if i != 'x'])
    base = set(str(i) for i in range(10)) - nums

    poss = []
    for perm in ps(base):
        out = problem.replace('x', '{}').format(*perm)
        nums = list(map(int, out.split()[::2]))
        if sum(nums[:2]) == nums[2]:
            poss.append('{} + {} = {}'.format(*nums))

    return poss


def main():
    inp = [
        '1xx + xxx = 468',
        'xxx + x81 = 9x4',
        'xxx + 5x1 = 86x',
        'xxx + 39x = x75',
    ]

    for i in inp:
        print(mathagram(i))


if __name__ == '__main__':
    main()
