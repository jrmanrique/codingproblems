# https://projecteuler.net/problem=30

from euler.typetools import get_digits


def main():
    limit = 10 ** 6
    nth = 5

    solutions = []
    for n in range(10, limit):
        if n == sum(list(map(lambda x: x ** nth, get_digits(n)))):
            solutions.append(n)
            print(solutions)
    print(sum(solutions))


if __name__ == '__main__':
    main()
