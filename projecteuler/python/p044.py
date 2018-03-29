# https://projecteuler.net/problem=44

def get_nth_pentagonal(n):
    return n * (3 * n - 1) // 2


def main():
    limit = 10 ** 2
    pentags = [1]
    best = 10 ** 10
    for i in range(2, limit):
        new = get_nth_pentagonal(i)
        pentags.append(new)
        for pen in pentags[-1::-1]:
            if abs(new - pen) < best:
                if abs(new - pen) == new + pen:
                    best = abs(new - pen)
                    print(best)
            else:
                break
    print(best)


if __name__ == '__main__':
    main()
