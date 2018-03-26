# https://www.reddit.com/r/dailyprogrammer/comments/3r7wxz/20151102_challenge_239_easy_a_game_of_threes/

import pprint as pp

from copy import deepcopy
from itertools import zip_longest as zip


def to_ternary(dec):
    def to_basen(dec, n):
        if dec == 0:
            return [0]
        digits = []
        while dec:
            dec, d = divmod(dec, n)
            digits.insert(0, d)
        return digits

    mapping = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return ''.join([mapping[i] for i in to_basen(dec, 3)])


def from_ternary(ter):
    def from_basen(basen, n):
        mults = [n ** i for i in range(len(basen))][::-1]
        return sum([int(i[0]) * i[1] for i in zip(basen, mults)])

    return from_basen(ter, 3)


def reverse_threes(seq):
    reverses = set()
    stack = [[1, seq]]
    while stack:
        num, queue = stack.pop()
        queue = deepcopy(queue)
        if queue:
            digit = queue.pop()
        else:
            reverses.add(num)
            continue
        for d in [digit * sign for sign in (-1, 1)]:
            stack.append([num * 3 + d, queue])

    return reverses


def threes(num):
    def get_move(num):
        tree = {0: [0], 1: [-1, 2], 2: [1, -2]}
        if num == 2:
            return [1]
        return tree[num % 3]

    solutions = []
    stack = [([num], get_move(num), [])]
    while stack:
        path, moves, real = stack.pop()
        if path[-1] == 1:
            solutions.append(real)
            continue
        for move in moves:
            new = (path[-1] + move) // 3
            stack.append((path + [new], get_move(new), real + [move]))

    return solutions


def decode(dec):
    """
    Return all possible alphabet representation of a threes-encoded decimal.
    """

    decimal = [from_ternary(''.join(map(lambda x: str(abs(x)), t))) for t in threes(dec)]
    valid = [chr(c) for c in filter(lambda x: 65 <= x <= 90 or 97 <= x <= 122, decimal)]
    return valid


def encode(char):
    """
    Return all possible three-encoded decimal representation of a character.
    """

    return reverse_threes([int(i) for i in to_ternary(ord(char))])


def partition(collection):
    if len(collection) == 1:
        yield [collection]
        return

    first = collection[0]
    for smaller in partition(collection[1:]):
        for n, subset in enumerate(smaller):
            yield smaller[:n] + [[first] + subset] + smaller[n + 1:]
        yield [[first]] + smaller


def deep_flatten(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(deep_flatten(item))
        else:
            result.append(item)
    return result


def load_wordlist(file):
    with open(file, 'r') as f:
        wordlist = set(f.read().splitlines())
        wordlist |= set(['i', 'a'])
    return wordlist


def form_words(seq):
    formed = []
    stack = [[[], seq]]
    while stack:
        word, rem = stack.pop(0)
        word = deepcopy(word)
        rem = deepcopy(rem)
        if rem:
            nxt = rem.pop(0)
            for n in nxt:
                stack.append([word + [n], rem])
        else:
            formed.append(''.join(word))
    return formed


def decoder(dec):
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    coding = {c: set([d[0] for d in [(e, decode(e)) for e in encode(c)] if c in d[1]]) for c in chars}
    valid_encodes = set(deep_flatten(map(list, coding.values())))
    wordlist = load_wordlist('inputs/321_intermediate.in')

    inp = list(str(dec))
    check = set()
    for i, p in enumerate(partition(inp)):
        parts = list(map(lambda x: int(''.join(x)), p))
        if all([i in valid_encodes for i in parts]):
            check.add(' '.join([str(n) for n in parts]))

    found = set()
    for parts in check:
        letters = [decode(d) for d in map(int, parts.split())]
        words = list(filter(lambda x: x.lower() in wordlist, form_words(letters)))
        if words:
            for word in words:
                found.add(word.lower())

    return found


def main():
    inp = 134381472522
    print(decoder(inp))


if __name__ == '__main__':
    main()
