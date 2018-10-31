from euler.mathtools import phi


def resilience(n):
    return phi(n) / (n - 1)

def main():
    limit = 15499 / 94744

    i = 2
    while resilience(i) >= limit:
        i += 1
    print(i)

if __name__ == '__main__':
    main()
