# https://projecteuler.net/problem=4

def lennum(num):
    return len(str(num))


def isproduct(num):
    for div in range(100, 999):
        n, rem = divmod(num, div)
        if rem == 0:
            if lennum(n) == 3:
                return True, (n, div)
    return False, None


def ispalindrome(num):
    def _ispalindrome(string):
        if len(string) <= 1:
            return True
        elif string[0] == string[-1]:
            return _ispalindrome(string[1:-1])
        return False

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
