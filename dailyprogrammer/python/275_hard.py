# https://www.reddit.com/r/dailyprogrammer/comments/4so25w/20160713_challenge_275_intermediate_splurthian/?utm_term=52bffa82-b4a8-4e42-a5e1-71ec724ac1a5&utm_medium=search&utm_source=reddit&utm_name=dailyprogrammer&utm_content=79

from itertools import chain, combinations


def get_powerset(seq, min_length=0, max_length=None):
    if max_length is None:
        max_length = len(seq)
    return list(map(lambda x: ''.join(x), chain.from_iterable([combinations(seq, r) for r in range(min_length, max_length + 1)])))


def get_symbols(element, min_length=2, max_length=2):
    return list(map(lambda x: ''.join(x).capitalize(), get_powerset(element.lower(), min_length=min_length, max_length=max_length)))


def assign_symbol(element, seen):
    for symbol in get_symbols(element):
        if symbol not in seen:
            return symbol
    return None


def assign_elements(seq):
    def _assign_elements(seq):
        symbols = []
        for elm in seq:
            symbols.append((elm, assign_symbol(elm, [s[1] for s in symbols])))
        return symbols, [s[0] for s in symbols if s[1] is None]

    symbols, unassigned = _assign_elements(seq)

    while unassigned:
        for u in unassigned:
            seq.remove(u)
            seq.insert(0, u)
        symbols, unassigned = _assign_elements(seq)

    return symbols


def main():
    from math import log10
    from random import sample

    def scorer(assignments):
        seq = sorted(assignments, key=lambda x: x[0], reverse=True)
        symbs = [s[1] for s in seq]
        for i, s in enumerate(symbs[1:]):
            if s.lower() < symbs[i].lower():
                return i

    with open('inputs/275_hard.in', 'r') as f:
        random = f.read().splitlines()

    PASSES = 100
    width = int(log10(PASSES - 1)) + 1

    for i in range(PASSES):
        elements = sorted(sample(random, 676))
        symbols = assign_elements(elements)
        score = scorer(symbols)
        print('[Pass {:>{w}}] Score: {}'.format(i, score, w=width))


if __name__ == '__main__':
    main()
