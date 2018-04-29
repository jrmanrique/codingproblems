"""Given an array of integers, return a new array such that each
element at index i of the new array is the product of all the numbers
in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output
would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the
expected output would be [2, 3, 6].
"""

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
