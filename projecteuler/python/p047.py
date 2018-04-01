# https://projecteuler.net/problem=47

from euler.mathtools import get_prime_factors


def isdistinct(seq, length):
    def _isdistinct(a, b, length):
        x = set(get_prime_factors(a))
        y = set(get_prime_factors(b))
        if not x & y and len(x) == len(y) == length:
            return True
        return False

    return all([_isdistinct(*seq[i:i + 2], length) for i in range(len(seq) - 1)])


def main():
    limit = 10 ** 5
    cons = 4
    for i in range(limit, limit * 10 - cons + 2):
        hold = [j for j in range(i, i + cons)]
        if isdistinct(hold, cons):
            print(hold)
            break


if __name__ == '__main__':
    main()
