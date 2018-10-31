from euler.mathtools import sieve_of_atkin


def main():
    limit = 10 ** 6
    primes = sieve_of_atkin(limit)

    maxima = 0
    while primes:
        sigma = 0
        count = 0
        for p in primes:
            sigma += p
            count += 1
            if sigma in primes and count > maxima:
                maxima = count
                print(sigma)
            if sigma >= limit:
                break
        primes = primes[1:]


if __name__ == '__main__':
    main()
