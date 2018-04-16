# https://projecteuler.net/problem=31

def coinchange(n, coins):
    ways = []
    stack = [[n, [], coins]]
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
    ways = coinchange(200, [1, 2, 5, 10, 20, 50, 100, 200])
    print(len(ways))


if __name__ == '__main__':
    main()
