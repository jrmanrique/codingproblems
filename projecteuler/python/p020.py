# https://projecteuler.net/problem=20

def memoize(func):
    cache = {}
    def helper(x):
        if x not in cache:
            cache[x] = func(x)
        return cache[x]
    return helper


@memoize
def factorial(num):
    if num == 0:
        return 1
    elif num == 1:
        return 1
    else:
        return factorial(num - 1) * num


def main():
    num = 100
    print(sum([int(d) for d in str(factorial(num))]))


if __name__ == '__main__':
    main()
