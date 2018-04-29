"""Run-length encoding is a fast and simple method of encoding strings.
The basic idea is to represent repeated successive characters as a
single count and character. For example, the string "AAAABBBCCDAA"
would be encoded as "4A3B2C1D2A".

Implement run-length encoding and decoding. You can assume the string
to be encoded have no digits and consists solely of alphabetic
characters. You can assume the string to be decoded is valid.
"""

def encode(string):
    encoded = ''
    hold = [0, '']

    for c in string:
        if not hold[1]:
            hold = [0, c]

        if c == hold[1]:
            hold[0] += 1
        else:
            encoded += '{}{}'.format(*hold)
            hold = [1, c]

    if hold[1]:
        encoded += '{}{}'.format(*hold)

    return encoded


def decode(string):
    hold = [string[i:i + 2] for i in range(0, len(string), 2)]
    return ''.join([b * int(a) for a, b in hold])


def main():
    inps = [
        'AAAABBBCCDAA',
    ]

    for inp in inps:
        enc = encode(inp)
        print('{} => {} ({})'.format(
            inp,
            enc,
            'Verified' if decode(enc) == inp else 'Failed'
        ))


if __name__ == '__main__':
    main()
