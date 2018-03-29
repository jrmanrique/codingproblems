# https://projecteuler.net/problem=1

def main():
    maxima = 1000
    sigma = sum([i for i in range(1, maxima) if i % 3 == 0 or i % 5 == 0])
    print(sigma)


if __name__ == '__main__':
    main()
