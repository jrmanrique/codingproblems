# Power of Cryptography

import math


def k(n, p):
    return round(math.pow(math.e, math.log(p) / n))


def main():
    while True:
        try:
            n = int(input())
            p = int(input())
        except EOFError:
            break
        else:
            print(k(n, p))


if __name__ == '__main__':
    main()
