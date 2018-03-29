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


def main():
    with open('inputs/275_intermediate.in', 'r') as f:
        elements = f.read().splitlines()

    symbols = []
    for element in elements:
        symbols.append((element, assign_symbol(element, [s[1] for s in symbols])))

    for s in symbols:
        print('{}: {}'.format(*s))

    print()
    print('Unassigned:', [s[0] for s in symbols if s[1] is None])


def bonus():
    def assign_elements(seq):
        symbols = []
        for elm in seq:
            symbols.append((elm, assign_symbol(elm, [s[1] for s in symbols])))
        return symbols, [s[0] for s in symbols if s[1] is None]


    with open('inputs/275_intermediate.in', 'r') as f:
        elements = f.read().splitlines()

    elements.sort(key=lambda x: len(get_symbols(x)))

    symbols, unassigned = assign_elements(elements)

    while unassigned:
        for u in unassigned:
            elements.remove(u)
            elements.insert(0, u)
        symbols, unassigned = assign_elements(elements)

    for s in symbols:
        print('{}: {}'.format(*s))


if __name__ == '__main__':
    main()
    bonus()
