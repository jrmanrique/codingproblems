# https://projecteuler.net/problem=57

def main():
    from math import log10

    counter = 0
    n, d = 3, 2
    for _ in range(2, 1000 + 1):
        if int(log10(n)) > int(log10(d)):
            counter += 1
        n, d = n + 2 * d, n + d
    print(counter)


if __name__ == '__main__':
    main()
