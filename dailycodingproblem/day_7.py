"""Given the mapping a = 1, b = 2, ... z = 26, and an encoded message,
count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded
as 'aaa', 'ka', and 'ak'.
"""

from collections import deque
from random import randint


def generate_input(width):
    inp = str(randint(1, 9))
    for _ in range(width - 1):
        if inp[-1] in ['1', '2']:
            inp += str(randint(0, 9))
        else:
            inp += str(randint(1, 9))
    return inp


def encode(string):
    return ''.join([str(ord(c) - 96) for c in string])


def decode(string):
    solutions = []
    queue = deque([[[], string]])
    while queue:
        path, rem = queue.popleft()
        if rem:
            if 10 <= int(rem[:2]) <= 26:
                if len(rem[:3]) == 3 and int(rem[:3]) % 10 == 0:
                    queue.append([path + [int(rem[0])], rem[1:]])
                    continue
                queue.append([path + [int(rem[:2])], rem[2:]])
                if int(rem[:2]) % 10 == 0:
                    continue
            queue.append([path + [int(rem[0])], rem[1:]])
        else:
            solutions.append(path)
    return solutions


def main():
    # inp = generate_input(randint(5, 15))
    inp = encode('dailycoding')

    sol = decode(inp)
    print('"{}" has {} way{} of being decoded.'.format(inp, len(sol), '' if len(sol) == 1 else 's'))
    decodes = [''.join([chr(o + 96) for o in s]) for s in sol]
    print(decodes)
    assert all([char.isalpha() for char in ''.join(decodes)])


if __name__ == '__main__':
    main()
