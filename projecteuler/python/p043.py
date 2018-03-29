# https://projecteuler.net/problem=43

from itertools import permutations


def generate_pandigitals(length, start=1):
    digits = [i for i in range(start, length + 1)][::-1]
    return (int(''.join(map(str, p))) for p in permutations(digits))


def check_subdiv(num):
    def subdivide(num, start, end):
        return int(''.join([str(c) for c in str(num)[start:end + 1]]))

    primes = [1, 2, 3, 5, 7, 11, 13, 17]

    for i in range(1, 7 + 1):
        n = subdivide(num, i, i + 2)
        if n % primes[i]:
            return False
    return True


def main():
    total = 0
    for pand in generate_pandigitals(9, start=0):
        if pand < 10 * 9:
            continue
        else:
            if check_subdiv(pand):
                total += pand
                print(pand, total)


if __name__ == '__main__':
    main()
