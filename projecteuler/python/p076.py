# https://projecteuler.net/problem=76

from collections import deque


def coinchange(n, coins):
    ways = []
    stack = deque([[n, [], coins]])
    while stack:
        rem, change, coins = stack.pop()
        if rem == 0:
            ways.append(change)
            continue
        sort = list(filter(lambda x: x <= rem, coins))
        for coin in sort:
            stack.append([
                rem - coin,
                change + [coin],
                list(filter(lambda x, maxima=coin: x <= maxima, sort))
            ])
    return ways


def main():
    number = 100
    print(len(coinchange(number, range(1, number))))


if __name__ == '__main__':
    main()
