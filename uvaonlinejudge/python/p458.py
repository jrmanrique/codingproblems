# The Decoder


def shift(string, n):
    return ''.join([chr(ord(c) + n) if c != '\n' else '\n' for c in string])


def main():
    while True:
        try:
            line = input()
        except EOFError:
            break
        else:
            print(shift(line, -7))


if __name__ == '__main__':
    main()
