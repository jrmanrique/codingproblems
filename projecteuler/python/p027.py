# https://projecteuler.net/problem=27

from euler.mathtools import isprime


def get_next_prime(num):
    while not isprime(num + 1):
        num += 1
    return num + 1


def main():
    limit = 1000

    primes = [2]
    while primes[-1] < limit:
        primes.append(get_next_prime(primes[-1]))
    seqb = primes[:-1]

    best = ((0, 0), 0)
    for b in seqb:
        if b == 2:
            seqa = [i for i in range(-limit + 1, limit) if i % 2 == 0]
        else:
            seqa = [i for i in range(-limit, limit + 1) if i % 2 == 1]
        for a in seqa:
            count = 0
            n = 0
            while True:
                if isprime(n ** 2 + a * n + b):
                    count += 1
                    if count > best[1]:
                        best = ((a, b), n)
                    n += 1
                else:
                    break

    print(best, best[0][0] * best[0][1])


if __name__ == '__main__':
    main()
