# https://www.reddit.com/r/dailyprogrammer/comments/4savyr/20160711_challenge_275_easy_splurthian_chemistry/

from itertools import chain, combinations


def get_powerset(seq, min_length=0, max_length=None):
    if max_length is None:
        max_length = len(seq)
    return list(map(lambda x: ''.join(x), chain.from_iterable([combinations(seq, r) for r in range(min_length, max_length + 1)])))


def get_symbols(element, min_length=2, max_length=2):
    return list(map(lambda x: ''.join(x).capitalize(), get_powerset(element.lower(), min_length=min_length, max_length=max_length)))


def main():
    inp = [
        ('Spenglerium', 'Ee'),
        ('Zeddemorium', 'Zr'),
        ('Venkmine', 'Kn'),
        ('Stantzon', 'Zt'),
        ('Melintzum', 'Nn'),
        ('Tullium', 'Ty'),
    ]

    for i in inp:
        word, sym = i
        print('{}, {} => {}'.format(*i, sym in get_symbols(word)))


def bonus_1():
    inp = [
        'Gozerium',
        'Slimyrine',
    ]

    for word in inp:
        print('{} => {}'.format(word, sorted(get_symbols(word))[0]))


def bonus_2():
    inp = [
        'Zuulon',
    ]

    for word in inp:
        print('{} => {}'.format(word, len(get_symbols(word))))


def bonus_3():
    inp = [
        'Zuulon',
    ]

    for word in inp:
        print('{} => {}'.format(word, len(get_symbols(word, min_length=1, max_length=len(word)))))




if __name__ == '__main__':
    main()
    bonus_1()
    bonus_2()
    bonus_3()
