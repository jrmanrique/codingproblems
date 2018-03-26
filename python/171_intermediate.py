# https://www.reddit.com/r/dailyprogrammer/comments/2avd5i/7162014_challenge_171_intermediate_zoom_rotate/

h2i = __import__('171_easy')


def string(seq, sep=''):
    return sep.join(seq)


def rotate(hexs, clockwise=True):
    matrix = h2i.hex_to_bin(hexs)

    r = len(matrix)
    c = len(matrix[0])

    if clockwise:
        cols = range(c)
        rows = range(r - 1, -1, -1)
    else:
        cols = range(c - 1, -1, -1)
        rows = range(r)

    return h2i.bin_to_hex([string([matrix[row][col] for row in rows]) for col in cols])


def invert(hexs):
    transtab = h2i.maketrans(['0', '1'], ['1', '0'])
    return h2i.bin_to_hex(list(map(lambda x: x.translate(transtab), h2i.hex_to_bin(hexs))))


def zoom_in(hexs):
    def dupe(seq):
        return [i for i in seq for _ in (0, 1)]

    return h2i.bin_to_hex(dupe(map(lambda x: string(dupe(x)), h2i.hex_to_bin(hexs))))


def zoom_out(hexs):
    def compress(seq):
        return [c for i, c in enumerate(seq) if i % 2]

    return h2i.bin_to_hex(compress(map(lambda x: string(compress(x)), h2i.hex_to_bin(hexs))))


def main():
    inputs = [
        '18 3C 7E 7E 18 18 18 18',
        'FF 81 BD A5 A5 BD 81 FF',
        'AA 55 AA 55 AA 55 AA 55',
        '3E 7F FC F8 F8 FC 7F 3E',
        '93 93 93 F3 F3 93 93 93',
    ]

    for inp in inputs:
        inp = inp.split()

        inp = zoom_in(inp)
        inp = zoom_in(inp)
        inp = rotate(inp)
        inp = zoom_in(inp)
        inp = zoom_in(inp)
        inp = invert(inp)
        inp = zoom_out(inp)
        inp = zoom_out(inp)

        print(*h2i.hex_to_img(inp, on='█', off='░'), sep='\n')
        print()


if __name__ == '__main__':
    main()
