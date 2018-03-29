# https://projecteuler.net/problem=55

from itertools import permutations


def ispalindrome(num):
    def _ispalindrome(s):
        if len(s) < 2:
            return True
        if s[0] == s[-1]:
            return _ispalindrome(s[1:-1])
        return False

    return _ispalindrome(str(num))


def permutepal(start):
    def permute(num):
        return (int(''.join(p)) for p in permutations(str(num)))

    def combine(num):
        return ((num, p) for p in permute(num) if p != num)


    stack = [[[], start]]
    while stack:
        path, num = stack.pop(0)
        if ispalindrome(num):
            return path, num
        if len(path) >= 50:
            continue
        for comb in combine(num):
            stack.append([path + [comb], sum(comb)])

    return None


def reverse(num):
    return int(''.join([d for d in str(num)[::-1]]))


def reversepal(num):
    path = [(num, reverse(num))]

    while len(path) < 50:
        pal = sum(path[-1])
        if ispalindrome(pal):
            return path
        else:
            path.append((pal, reverse(pal)))
    return None


def main():
    counter = 0
    for n in range(1, 10 ** 4):
        if reversepal(n) is None:
            counter += 1
    print(counter)


if __name__ == '__main__':
    main()
