# Jolly Jumpers

def diff(seq):
    return [abs(num - seq[i + 1]) for i, num in enumerate(seq[:-1])]


def main():
    while True:
        try:
            inp = input()
        except EOFError:
            break
        else:
            n, *seq = [int(d) for d in inp.split()]
            print('Jolly' if sorted(diff(seq)) == list(range(1, n)) else 'Not jolly')


if __name__ == '__main__':
    main()
