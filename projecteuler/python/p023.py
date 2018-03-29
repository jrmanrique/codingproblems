# https://projecteuler.net/problem=23

from math import sqrt


def proper_divisor(num):
    yield 1

    largest = int(sqrt(num))
    if largest ** 2 == num:
        yield largest
    else:
        largest += 1

    for div in range(2, largest):
        n, r = divmod(num, div)
        if r == 0:
            yield div
            yield n


def isabundant(num):
    return num < sum(proper_divisor(num))


def isabsum(num, abundants):
    abunds = set(filter(lambda x: x < num, abundants))
    for i in abunds:
        if num - i in abunds:
            return True
    return False


def main():
    limit = 28123

    abundants = [i for i in range(1, limit + 1) if isabundant(i)]

    total = 0
    for num in range(1, limit + 1):
        if not isabsum(num, abundants):
            total += num

    print(total)


if __name__ == '__main__':
    main()
