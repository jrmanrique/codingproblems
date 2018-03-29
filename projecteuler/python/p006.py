# https://projecteuler.net/problem=6

def main():
    maxima = 100
    numbers = [i for i in range(1, maxima + 1)]
    sum_squares = sum([pow(n, 2) for n in numbers])
    square_sums = pow(sum(numbers), 2)
    print(sum_squares - square_sums)


if __name__ == '__main__':
    main()
