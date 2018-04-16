# https://www.reddit.com/r/dailyprogrammer/comments/8bh8dh/20180411_challenge_356_intermediate_goldbachs/

def sieve(limit):
    sieve = {n: True for n in range(2, limit + 1)}
    for n in range(2, limit + 1):
        if sieve[n]:
            for a in range(2, limit // n + 1):
                sieve[n * a] = False
    return [k for k, v in sieve.items() if v]


def goldbach(num):
    for a in sieve(num):
        for b in sieve(a):
            for c in sieve(b):
                if a + b + c == num:
                    return a, b, c
    return None


def main():
    print(goldbach(15))


if __name__ == '__main__':
    main()
