import pickle

from collections import deque


def get_subtree(word, trie):
    parent = trie
    for char in word:
        try:
            parent = parent[char]
        except KeyError:
            parent = {}
    return parent


def isword(word, trie):
    try:
        return get_subtree(word, trie)['isword']
    except KeyError:
        return False


def get_words(substr, trie):
    words = []
    if isword(substr, trie):
        words.append(substr)

    root = get_subtree(substr, trie)
    queue = deque([[substr, c] for c in root if c != 'isword'])
    while queue:
        path, char = queue.popleft()
        word = path + char
        if isword(word, trie):
            words.append(word)
        for child in get_subtree(word, trie):
            if child == 'isword':
                continue
            queue.append([word, child])

    return words


def main():
    substring = 'pyt'
    trie = pickle.load(open('tests/words_trie.pkl', 'rb'))
    print(get_words(substring, trie))


if __name__ == '__main__':
    main()
