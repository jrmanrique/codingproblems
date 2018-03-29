# https://www.reddit.com/r/dailyprogrammer/comments/19mn2d/030413_challenge_121_easy_bytelandian_exchange_1/

def main():
    cache = {0: 1}

    def exchange(coin):
        if coin not in cache:
            cache[coin] = exchange(coin // 4) + exchange(coin // 3) + exchange(coin // 2)
        return cache[coin]

    print(exchange(10 ** 9))


if __name__ == '__main__':
    main()
