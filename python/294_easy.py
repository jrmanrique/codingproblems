# https://www.reddit.com/r/dailyprogrammer/comments/5go843/20161205_challenge_294_easy_rack_management_1/

def ispossible(tiles, word):
    tiles = list(tiles)
    free_tiles = tiles.count('?')

    for char in word:
        try:
            tiles.remove(char)
        except ValueError:
            free_tiles -= 1

        if free_tiles < 0:
            return False

    return True


def get_points(tiles, word):
    POINTS = [
        1, 3, 3, 2, 1, 4, 2, 4, 1, 8,
        5, 1, 3, 1, 1, 3, 10, 1, 1, 1,
        1, 4, 4, 8, 4, 10
    ]

    score = 0
    tiles = list(tiles)
    free_tiles = tiles.count('?')

    for char in word:
        try:
            tiles.remove(char)
            score += POINTS[ord(char) - 97]
        except ValueError:
            free_tiles -= 1

        if free_tiles < 0:
            return None
    return score


def get_valid_words(tiles, wordlist):
    return [(w, get_points(tiles, w)) for w in wordlist if get_points(tiles, w)]


def get_best(tiles, wordlist):
    return sorted(get_valid_words(tiles, wordlist), key=lambda x: x[1], reverse=True)[0]


def main():
    inputs = [
        'ladilmy daily',
        'eerriin eerie',
        'orrpgma program',
        'orppgma program',
    ]

    for inp in inputs:
        tiles, word = inp.split()
        print('{} {} => {}'.format(tiles, word, ispossible(tiles, word)))


def bonus_1():
    inputs = [
        'pizza?? pizzazz',
        'piizza? pizzazz',
        'a?????? program',
        'b?????? program',
    ]

    for inp in inputs:
        tiles, word = inp.split()
        print('{} {} => {}'.format(tiles, word, ispossible(tiles, word)))


def bonus_2():
    inputs = [
        'dcthoyueorza',
        'uruqrnytrois',
        'rryqeiaegicgeo??',
        'udosjanyuiuebr??',
        'vaakojeaietg????????',
    ]

    with open('inputs/294_easy.in', 'r') as f:
        wordlist = set(f.read().splitlines())
        wordlist |= set(['i', 'a'])

    for inp in inputs:
        print('{} => {} ({})'.format(inp, *max(get_valid_words(inp, wordlist), key=lambda x: len(x[0]))))


def bonus_3():
    inputs = [
        'dcthoyueorza',
        'uruqrnytrois',
        'rryqeiaegicgeo??',
        'udosjanyuiuebr??',
        'vaakojeaietg????????',
    ]

    with open('inputs/294_easy.in', 'r') as f:
        wordlist = set(f.read().splitlines())
        wordlist |= set(['i', 'a'])

    for inp in inputs:
        print('{} => {} ({})'.format(inp, *get_best(inp, wordlist)))


if __name__ == '__main__':
    main()
    bonus_1()
    bonus_2()
    bonus_3()
