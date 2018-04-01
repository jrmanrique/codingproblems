# Kindergarten Counting Game

import re


def main():
    while True:
        try:
            line = input()
        except EOFError:
            break
        else:
            words = re.findall('[a-zA-Z]+', line)
            print(len(words))


if __name__ == '__main__':
    main()
