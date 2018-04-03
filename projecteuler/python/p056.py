# https://projecteuler.net/problem=56

from euler.helpers import get_digits


def main():
    best = (0, 0 ,0)
    for a in range(1, 100):
        for b in range(1, 100):
            ans = sum(get_digits(pow(a, b)))
            if ans > best[2]:
                best = (a, b, ans)

    print(best)


if __name__ == '__main__':
    main()
