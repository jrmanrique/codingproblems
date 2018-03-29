# https://projecteuler.net/problem=38

def get_digits(num):
    return [int(d) for d in str(num)]


def ispandigital(num):
    return sorted(get_digits(num)) == [i for i in range(1, 9 + 1)]


def get_concatenation(num, width):
    mults = [i for i in range(1, width + 1)]
    out = ''.join([str(num * m) for m in mults])
    return int(out), len(out)


def main():
    best = (0, (0, 0))
    for i in range(2, 9 + 1):
        for n in range(3, 10000):
            concat, check = get_concatenation(n, i)
            if check == 9 and ispandigital(concat):
                if best[0] < concat:
                    best = (concat, (n, i))
            elif check > 9:
                break
    print(best)


if __name__ == '__main__':
    main()
