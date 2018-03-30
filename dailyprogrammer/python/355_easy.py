# https://www.reddit.com/r/dailyprogrammer/comments/879u8b/20180326_challenge_355_easy_alphabet_cipher/

from itertools import cycle


def cipher(char, key, decipher=False):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    shift = ord(key.lower()) - 97
    if decipher:
        return alpha[(alpha[shift:] + alpha[:shift]).index(char.lower())]
    else:
        alpha = alpha[shift:] + alpha[:shift]
        return alpha[ord(char.lower()) - 97]


def encrypt(text, key):
    return ''.join(cipher(v, k) for v, k in zip(text, cycle(key)))


def decrypt(text, key):
    return ''.join(cipher(v, k, decipher=True) for v, k in zip(text, cycle(key)))


def main():
    inputs = [
        'snitch thepackagehasbeendelivered',
        'bond theredfoxtrotsquietlyatmidnight',
        'train murderontheorientexpress',
        'garden themolessnuckintothegardenlastnight',
    ]

    for inp in inputs:
        key, text = inp.split()
        print('{} {} => {}'.format(key, text, encrypt(text, key)))


def bonus():
    inputs = [
        'cloak klatrgafedvtssdwywcyty',
        'python pjphmfamhrcaifxifvvfmzwqtmyswst',
        'moore rcfpsgfspiecbcc',
    ]

    for inp in inputs:
        key, text = inp.split()
        print('{} {} => {}'.format(key, text, decrypt(text, key)))


if __name__ == '__main__':
    main()
    bonus()
