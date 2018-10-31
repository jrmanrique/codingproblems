# https://www.reddit.com/r/dailyprogrammer/comments/98ufvz/20180820_challenge_366_easy_word_funnel_1/
# https://www.reddit.com/r/dailyprogrammer/comments/99d24u/20180822_challenge_366_intermediate_word_funnel_2/

from collections import deque


def load_wordlist(file):
    with open(file, 'r') as f:
        wordlist = set(f.read().splitlines())
        # wordlist |= set(['i', 'a'])
    return wordlist


def funnel(word, wordlist):
    out = [word[:i] + word[i + 1:] for i, _ in enumerate(word)]
    return list(filter(lambda x: x in wordlist, out))


def longest_funnel(word, wordlist):
    solutions = []
    stack = deque([[word]])
    while stack:
        current = stack.pop()
        children = funnel(current[-1], wordlist)
        if children:
            for child in children:
                stack.append(current + [child])
        else:
            solutions.append(current)

    return sorted(solutions, key=len)[-1]


def main():
    wordlist = load_wordlist('inputs/enable1.in')
    length = 9

    for word in wordlist:
        if len(word) > length:
            sol = longest_funnel(word, wordlist)
            if len(sol) >= length:
                print(len(sol), sol)


if __name__ == '__main__':
    main()
