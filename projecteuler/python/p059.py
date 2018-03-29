# https://projecteuler.net/problem=59

from itertools import permutations as perm
from itertools import cycle


def load_file(file):
    with open(file, 'r') as f:
        data = f.read()
    return data


def xor(a, b):
    return int(bin(a), 2) ^ int(bin(b), 2)


def decrypt(text, key):
    return [xor(v, k) for v, k in zip(text, cycle(key))]


def chrseq(seq):
    return [chr(o) for o in seq]


def ordseq(seq):
    return [ord(char) for char in seq]


def allintext(text, seq):
    for subs in seq:
        if subs not in text:
            return False
    return True


def main():
    inp = load_file('inputs/p059.in')
    inp = [int(d) for d in inp.split(',')]

    wordlist = load_file('inputs/dict.in')
    wordlist = set(wordlist.splitlines() + ['i', 'a'])

    keys = perm([i for i in range(97, 122 + 1)], 3)

    error = 0.25
    possible = []
    for key in keys:
        dec = decrypt(inp, key)
        dec = ''.join(chrseq(dec)).split()
        counter = 0
        for word in dec:
            if word.lower() not in wordlist:
                counter += 1
            if counter > len(dec) * error:
                break
        else:
            possible.append((''.join(chrseq(key)), counter / len(dec)))
    print([s[0] for s in sorted(possible, key=lambda x: x[1])])


def test():
    from time import sleep

    inp = load_file('inputs/p059.in')
    inp = [int(d) for d in inp.split(',')]

    keys = ['god']  # 25% error check.

    for key in keys:
        dec = decrypt(inp, ordseq(key))
        print(''.join(chrseq(dec)))
        print('=== {}: {} ==='.format(key, sum(dec)))
        sleep(2)


if __name__ == '__main__':
    main()
    test()
