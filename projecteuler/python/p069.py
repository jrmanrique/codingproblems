# https://projecteuler.net/problem=69

def sieve(num):
    sieve = {n: True for n in range(2, num + 1)}
    for n in range(2, num + 1):
        if sieve[n]:
            for a in range(2, num // n + 1):
                sieve[n * a] = False
    return [k for k, v in sieve.items() if v]


def main():
    primes = sieve(10 ** 6)

    large = 1
    i = 0
    while large < 10 ** 6:
        large *= primes[i]
        i += 1
    print(large // primes[i-1])


if __name__ == '__main__':
    main()
