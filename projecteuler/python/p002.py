# https://projecteuler.net/problem=2

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


def main():
    maxima = 4 * 10 ** 6

    fibs = [0]
    i = 1
    while fibs[-1] < maxima:
        fibs.append(fibonnaci(i))
        i += 1

    fibs = fibs[:-1]

    sigma = sum([f for f in fibs if f % 2 == 0])
    print(sigma)


if __name__ == '__main__':
    main()
