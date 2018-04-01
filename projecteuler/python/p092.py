# https://projecteuler.net/problem=92

from collections import Counter
from functools import lru_cache, reduce
from math import factorial as f
from operator import mul


@lru_cache()
def ss_digits(num):
    return sum(map(lambda x: pow(int(x), 2), str(num)))


def multinomial(num, width=None):
    def _get_digits(num):
        return map(int, str(num))

    if width is None:
        width = len(str(num))
    c = Counter(_get_digits(num))
    return f(width) // reduce(mul, [f(v) for v in c.values()])


def generate_multisets(width):
    def _ltoi(seq):
        return int(''.join([str(d) for d in seq]))

    num = [0] * width
    ptr = width - 1
    while True:
        if ptr == 0 and num[ptr] == 9:
            break
        if ptr == width - 1 and num[ptr] < 9:
            num[ptr] += 1
            yield _ltoi(num)
        elif num[ptr] == 9:
            ptr -= 1
        else:
            num[ptr] += 1
            for i in range(ptr + 1, width):
                num[i] = num[ptr]
            ptr = width - 1
            yield _ltoi(num)


def main():
    limit = 7

    counter = 0
    cache = {}
    for i in generate_multisets(limit):
        num = i
        while num not in (1, 89):
            if num not in cache:
                cache[num] = ss_digits(num)
            num = cache[num]
        if num == 89:
            counter += multinomial(i, limit)

    print(counter)
    print('CORRECT ANSWER:', counter == 8581146)


if __name__ == '__main__':
    main()
