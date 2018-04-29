"""Given a string of round, curly, and square open and closing
brackets, return whether the brackets are balanced (well-formed).

For example, given the string "([])[]({})", you should return true.

Given the string "([)]" or "((()", you should return false.
"""

def is_balanced(string):
    track = ''
    for c in string:
        if c in '({[':
            track += c
        elif c in ')}]':
            if track[-1] + c in ['()', '{}', '[]']:
                track = track[:-1]
            else:
                return False
    return not track


def main():
    inps = [
        '([])[]({})',
        '([)]',
        '((()',
    ]

    for inp in inps:
        print('{} => {}'.format(inp, is_balanced(inp)))


if __name__ == '__main__':
    main()
