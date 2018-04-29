"""The edit distance between two strings refers to the minimum number
of character insertions, deletions, and substitutions required to
change one string to the other. For example, the edit distance between
“kitten” and “sitting” is three: substitute the “k” for “s”, substitute
the “e” for “i”, and append a “g”.

Given two strings, compute the edit distance between them.
"""

def edit_distance(stra, strb):
    m = len(stra)
    n = len(strb)

    if m == 0:
        return n
    elif n == 0:
        return m

    if stra[-1] == strb[-1]:
        return edit_distance(stra[:-1], strb[:-1])
    return 1 + min([
        edit_distance(stra[:-1], strb[:-2]),  # Insert
        edit_distance(stra[:-2], strb[:-1]),  # Remove
        edit_distance(stra[:-2], strb[:-2]),  # Replace
    ])


def main():
    inps = [
        ('geek', 'gesek'),
        ('cat', 'cut'),
        ('sunday', 'saturday'),
        ('kitten', 'sitting'),
    ]

    for inp in inps:
        print('{}, {} => {}'.format(*inp, edit_distance(*inp)))


if __name__ == '__main__':
    main()
