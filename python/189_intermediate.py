# https://www.reddit.com/r/dailyprogrammer/comments/2ms946/20141119_challenge_189_intermediate_roman_numeral/

def get_value(char):
    CHARS = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }
    return CHARS[char]


def from_roman(roman):
    CHARS = 'IVXLCDM'
    seq = [c for c in roman]
    total = 0
    while seq:
        a_idx = CHARS.index(seq[0])
        try:
            b = seq[1]
        except IndexError:
            pass
        else:
            if b in CHARS[a_idx + 1:]:
                total -= get_value(seq[0])
                seq.pop(0)
        finally:
            total += get_value(seq[0])
            seq.pop(0)
    return total


def to_roman(num):
    def rreplace(s, old, new):
        return new.join(s.rsplit(old, 1))

    CHARS = 'MDCLXVI'
    roman = ''

    while num != 0:
        for char in CHARS:
            value = get_value(char)
            if value <= num:
                num -= value
                roman += char
                break

    roman = rreplace(roman, 'III', 'V')
    roman = rreplace(roman, 'XXX', 'L')
    roman = rreplace(roman, 'CCC', 'D')
    roman = rreplace(roman, 'VIV', 'IX')
    roman = rreplace(roman, 'LXL', 'XC')
    roman = rreplace(roman, 'DCD', 'CM')

    return roman


def main():
    inputs = [
        'IV',
        'XXXIV',
        'CCLXVII',
        'DCCLXIV',
        'CMLXXXVII',
        'MCMLXXXIII',
        'MMXIV',
        'MMMM',
        'MMMMCMXCIX',
    ]

    for inp in inputs:
        print('{} => {}'.format(inp, from_roman(inp)))


if __name__ == '__main__':
    main()
