# Odd Sum


def main():
    t = int(input())
    for n in range(t):
        try:
            a = int(input())
            b = int(input())
        except EOFError:
            break
        else:
            if a > b:
                a, b = b, a
            start = a if a % 2 else a + 1
            print('Case {}: {}'.format(n + 1, sum([n for n in range(start, b + 1, 2)])))


if __name__ == '__main__':
    main()
