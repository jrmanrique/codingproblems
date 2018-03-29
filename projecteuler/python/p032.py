# https://projecteuler.net/problem=32

def get_digits(seq):
    result = []
    for n in seq:
        result.extend([int(d) for d in str(n)])
    return result


def ispandigital(seq):
    seq = get_digits(seq)
    if len(seq) != 9:
        return False
    return sorted(seq) == [i for i in range(1, 9 + 1)]


def main():
    pandigitals = set()
    for a in range(1, 99):
        for b in range(100, 9999):
            if ispandigital([a, b, a * b]):
                pandigitals.add(a * b)

    print(sum(pandigitals))


if __name__ == '__main__':
    main()
