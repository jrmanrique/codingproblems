# https://projecteuler.net/problem=29

def main():
    width = 100
    seq = set()
    for a in range(2, width + 1):
        for b in range(2, width + 1):
            seq.add(a ** b)

    print(len(seq))


if __name__ == '__main__':
    main()
