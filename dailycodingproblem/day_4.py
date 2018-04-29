"""Given an array of integers, find the first missing positive integer
in linear time and constant space. In other words, find the lowest
positive integer that does not exist in the array. The array can
contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0]
should give 3.
"""

def main():
    inputs = [
        '3 4 -1 1',
        '1 2 0',
    ]

    for inp in inputs:
        inp = sorted([int(d) for d in inp.split()])
        expected = 1
        for d in inp:
            if d > 0:
                if d == expected:
                    expected += 1
                else:
                    break
        print('{} => {}'.format(inp, expected))



if __name__ == '__main__':
    main()
