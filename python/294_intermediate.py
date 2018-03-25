# https://www.reddit.com/r/dailyprogrammer/comments/5h40ml/20161207_challenge_294_intermediate_rack/

def get_wordlist(file):
    with open(file, 'r') as f:
        wordlist = set(f.read().splitlines())
        wordlist |= set(['i', 'a'])
    return wordlist


def get_points(tiles, word):
    POINTS = [
        1, 3, 3, 2, 1, 4, 2, 4, 1, 8,
        5, 1, 3, 1, 1, 3, 10, 1, 1, 1,
        1, 4, 4, 8, 4, 10
    ]

    score = 0
    tiles = list(tiles)
    free_tiles = tiles.count('?')

    for i, char in enumerate(word):
        try:
            tiles.remove(char)
            score += (POINTS[ord(char) - 97] * (i + 1))
        except ValueError:
            free_tiles -= 1

        if free_tiles < 0:
            return None
    return score


def get_valid_words(tiles, wordlist):
    return [(w, get_points(tiles, w)) for w in wordlist if get_points(tiles, w)]


def get_best(tiles, wordlist):
    valid = get_valid_words(tiles, wordlist)
    if valid:
        return sorted(valid, key=lambda x: x[1], reverse=True)[0]
    else:
        return (None, 0)


def generate_trie(wordlist):
    trie = dict()
    for word in wordlist:
        parent = trie
        for i, char in enumerate(word):
            if char not in parent:
                parent[char] = dict()
            parent = parent[char]
            if i == len(word) - 1:
                parent['isword'] = True
            elif 'isword' not in parent.keys():
                parent['isword'] = False
    return trie


def depth_first(tiles, trie):
    def retrieve(trie, word):
        parent = trie
        seq = [c for c in word]
        while seq:
            try:
                parent = parent[seq[0]]
            except KeyError:
                return None
            else:
                seq.pop(0)
        return parent

    def score(word):
        POINTS = [
            1, 3, 3, 2, 1, 4, 2, 4, 1, 8,
            5, 1, 3, 1, 1, 3, 10, 1, 1, 1,
            1, 4, 4, 8, 4, 10
        ]
        return sum([POINTS[ord(c) - 97] * (i + 1) for i, c in enumerate(word)])

    def subtract_list(a, b):
        for i in b:
            if i in a:
                a.remove(i)
        return a


    best = (0, None)
    stack = [[n] for n in tiles]
    while stack:
        path = stack.pop()
        if retrieve(trie, path):
            if retrieve(trie, path)['isword']:
                word = ''.join(path)
                points = score(word)
                best = (points, word) if points > best[0] else best
        else:
            continue
        for unseen in subtract_list([c for c in tiles], path):
            stack.append(path + [unseen])
    return best


def main():
    inputs = [
        'iogsvooely',
        'seevurtfci',
        'vepredequi',
        'umnyeoumcp',
        'orhvtudmcz',
        'fyilnprtia',
    ]

    wordlist = get_wordlist('inputs/294_easy.in')

    for inp in inputs:
        print('{} => {} ({})'.format(inp, *get_best(inp, wordlist)))


def bonus_1():
    with open('inputs/294_intermediate.in', 'r') as f:
        inputs = f.read().splitlines()

    wordlist = get_wordlist('inputs/294_easy.in')
    trie = generate_trie(wordlist)

    for i, inp in enumerate(inputs):
        out = '{} => {} ({})'.format(inp, *depth_first(inp, trie))
        print('{:<30} | {:,} of {:,} ({:.2f}%)'.format(out, i, len(inputs), (i / len(inputs)) * 100))


def bonus_2():
    inputs = [
        'yleualaaoitoai??????',
        'afaimznqxtiaar??????',
        'yrkavtargoenem??????',
        'gasfreubevuiex??????',
    ]

    wordlist = get_wordlist('inputs/294_easy.in')

    for i, inp in enumerate(inputs):
        print('{} => {} ({})'.format(inp, *get_best(inp, wordlist)))


if __name__ == '__main__':
    main()
    bonus_2()
    bonus_1()
