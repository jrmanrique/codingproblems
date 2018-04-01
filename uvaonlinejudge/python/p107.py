# The Cat in the Hat

from math import log


def findn(height, working):
    for m in range(1, height):
        if height == round(pow(pow(working, 1 / m) + 1, m)):
            return round(pow(working, 1 / m))
    return 0


def notworking(height, n):
    try:
        return sum([n ** i for i in range(round(log(height, n + 1)))])
    except (ZeroDivisionError, ValueError):
        return 0


def totalheight(height, working, n):
    return n * (height - working) + height


def main():
    while True:
        try:
            inp = input()
        except EOFError:
            break
        else:
            height, working = [int(d) for d in inp.split()]
            if (height, working) == (0, 0):
                break
            else:
                n = findn(height, working)
                print('{} {}'.format(notworking(height, n), totalheight(height, working, n)))


if __name__ == '__main__':
    main()
