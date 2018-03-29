# https://projecteuler.net/problem=25

def memoize(func):
    cache = {}
    def helper(x):
        if x not in cache:
            cache[x] = func(x)
        return cache[x]
    return helper


@memoize
def fibonnaci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonnaci(n - 1) + fibonnaci(n - 2)


def lend(num):
    return len([d for d in str(num)])


def main():
    i = 1
    while lend(fibonnaci(i)) < 1000:
        i += 1
    print(i)


if __name__ == '__main__':
    main()
