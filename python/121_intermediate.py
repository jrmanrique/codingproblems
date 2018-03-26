# https://www.reddit.com/r/dailyprogrammer/comments/19rkqr/030613_challenge_121_intermediate_bytelandian/


def main():
    cache = {}

    def exchange(coin):
        if coin not in cache:
            if coin // 4 + coin // 3 + coin // 2 > coin:
                cache[coin] = exchange(coin // 4) + exchange(coin // 3) + exchange(coin // 2)
            else:
                cache[coin] = coin
        return cache[coin]

    print(exchange(10 ** 10))
    print(cache)


if __name__ == '__main__':
    main()
