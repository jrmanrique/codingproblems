# https://www.reddit.com/r/dailyprogrammer/comments/7z8hrm/20180221_challenge_352_intermediate_7_wonders/

import re

from collections import Counter


def input_case(a=None):
    if a is None:
        a = input()
    b, c = a.split('.')
    cards = [''.join(re.findall('[a-zA-Z]+', item)) for item in b.split()[1:]]
    reqs = ''.join(re.findall('[a-zA-Z]+', c.split()[-1]))
    return cards, reqs


def allocate(cards, reqs):
    avail_counter = Counter(list(''.join(cards)))
    rarity = sorted(avail_counter.items(), key=lambda x: x[1])
    rarity_list = [resource[0] for resource in rarity]

    req = [[req, None] for req in sorted(list(reqs), key=rarity_list.index)]
    hand = [[card, False] for card in sorted(cards, key=len)]

    for res in req:
        for card in hand:
            if res[0] in card[0] and not card[1]:
                res[1] = card[0]
                card[1] = True
                break

    return hand, req


def is_allocable(cards, reqs, verbose=False):
    hand, reqd = allocate(cards, reqs)
    if all([req[1] for req in reqd]):
        if all([card[1] for card in hand]):
            if verbose:
                matches = [(req[0], '/'.join(list(req[1]))) for req in reqd]
                matches = sorted(matches, key=lambda x: reqs.index(x[0]))
                print(*matches, sep='\n')
            return True
        print('You should never see this.')
        return True
    return False


def main():
    cases = input_case()
    if is_allocable(*cases):
        print('Allocable!')
    else:
        print('Unallocable.')


if __name__ == '__main__':
    main()
