# https://projecteuler.net/problem=36

def ispalindrome(string):
    if len(string) <= 1:
        return True
    elif string[0] == string[-1]:
        return ispalindrome(string[1:-1])
    return False


def to_bin(dec):
    return bin(dec)[2:]


def main():
    total = 0
    for n in range(1, 10 ** 6):
        if ispalindrome(str(n)) and ispalindrome(to_bin(n)):
            total += n
            print(n, to_bin(n), total)


if __name__ == '__main__':
    main()
