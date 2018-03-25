# https://www.reddit.com/r/dailyprogrammer/comments/2ao99p/7142014_challenge_171_easy_hex_to_8x8_bitmap/

def maketrans(old, new):
    return dict(zip(map(ord, old), new))


def hex_to_bin(hexs):
    width = len(hexs[0]) * 4
    return list(map(lambda x: '{:0{w}b}'.format(int(x, 16), w=width), hexs))


def bin_to_hex(bins):
    width = len(bins[0]) // 4
    return list(map(lambda x: '{:0{w}x}'.format(int(x, 2), w=width).upper(), bins))


def hex_to_img(hexs, on='X', off=' '):
    return list(map(lambda x: x.translate(maketrans(['0', '1'], [off, on])), hex_to_bin(hexs)))


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
        print(*hex_to_img(inp, on='█', off='░'), sep='\n')
        print()


if __name__ == '__main__':
    main()
