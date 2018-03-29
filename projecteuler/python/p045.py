# https://projecteuler.net/problem=45

def get_nth_hex(n):
    return n * (2 * n - 1)


def get_nth_pen(n):
    return (n * (3 * n - 1)) / 2


def main():
    limit = 10 ** 5
    hexseq = set([get_nth_hex(i) for i in range(1, limit)])
    penseq = set([get_nth_pen(i) for i in range(1, limit)])

    print(hexseq & penseq)


if __name__ == '__main__':
    main()
