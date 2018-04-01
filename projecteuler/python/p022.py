# https://projecteuler.net/problem=22

from euler.helpers import load_file


def score(name):
    return sum([ord(char) - 96 for char in name.lower()])


def main():
    inp = load_file('inputs/p022.in')
    names = list(map(lambda x: x[1:-1], inp.split(',')))

    total = 0
    for i, name in enumerate(sorted(names)):
        total += score(name) * (i + 1)

    print(total)


if __name__ == '__main__':
    main()
