from functools import reduce
from operator import mul as multiply


def mul(seq):
    return reduce(multiply, seq)


def mult(seq):
    return [mul(seq[:i] + seq[i + 1:]) for i, _ in enumerate(seq)]


def main():
    inputs = [
        '1 2 3 4 5',
        '3 2 1',
    ]

    for inp in inputs:
        inp =  [int(i) for i in inp.split()]
        print('{} => {}'.format(inp, mult(inp)))


if __name__ == '__main__':
    main()
