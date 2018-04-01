# https://projecteuler.net/problem=4

from euler.typetools import ispalindrome as _ispalindrome


def isproduct(num):
    for div in range(100, 999):
        n, rem = divmod(num, div)
        if rem == 0:
            if n in range(100, 999):
                return True, (n, div)
    return False, None


def ispalindrome(num):
    return _ispalindrome(str(num))


def main():
    for n in range(998001, 10000 - 1, -1):
        if ispalindrome(n):
            prod, factors = isproduct(n)
            if prod:
                print(n, factors)
                break


if __name__ == '__main__':
    main()
