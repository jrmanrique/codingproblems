# https://projecteuler.net/problem=41

from itertools import permutations

from euler.mathtools import isprime


def generate_pandigitals(length):
    digits = [i for i in range(1, length + 1)][::-1]
    return (int(''.join(map(str, p))) for p in permutations(digits))


def main():
    for l in range(9, 0, -1):
        for p in generate_pandigitals(l):
            if isprime(p):
                print(p)
                break


if __name__ == '__main__':
    main()
