# https://projecteuler.net/problem=14

import matplotlib.pyplot as plt


def count_chain(num, cache):
    counter = 1
    while num != 1:
        if num not in cache:
            if num % 2:
                cache[num] = (3 * num) + 1
            else:
                cache[num] = num // 2
        num = cache[num]
        counter += 1
    return counter


def main():
    n = 10 ** 6
    cache = {}
    chains = [(i, count_chain(i, cache)) for i in range(1, n + 1)]
    print(max(chains, key=lambda x: x[1]))

    plot = False

    if plot:
        plt.style.use('ggplot')
        plt.plot([i[1] for i in chains], ',')
        plt.show()


if __name__ == '__main__':
    main()
