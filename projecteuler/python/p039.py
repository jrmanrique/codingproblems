# https://projecteuler.net/problem=39

def isvalid(a, b, c):
    return a ** 2 + b ** 2 == c ** 2


def get_valid_solutions(perim):
    counter = 0
    for a in range(1, perim // 3 + 1):
        for b in range(a, perim // 2 + 1):
            c = perim - a - b
            if isvalid(a, b, c):
                counter += 1
    return counter


def main():
    best = (0, 0)
    for i in range(300, 1000 + 1):
        sol = get_valid_solutions(i)
        if sol > best[0]:
            best = (sol, i)
    print(best)


if __name__ == '__main__':
    main()
