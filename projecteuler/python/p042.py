# https://projecteuler.net/problem=42

from euler.helpers import load_file


def score_word(word):
    score = 0
    for char in word:
        score += ord(char.lower()) - 96
    return score


def solve_quad(a, b, c):
    det = (b ** 2 - 4 * a * c) ** 0.5
    return ((-b + det) / (2 * a)), ((-b - det) / (2 * a))


def istriword(word):
    score = score_word(word)
    a, b = solve_quad(1, 1, -score * 2)
    try:
        if (a % 1 == 0 or b % 1 == 0) and (a > 0 or b > 0):
            return True
    except TypeError:
        return False
    return False


def main():
    inp = load_file('inputs/p042.in')
    inp = [i[1:-1] for i in inp.split(',')]

    counter = 0
    for w in inp:
        if istriword(w):
            counter += 1

    print(counter)



if __name__ == '__main__':
    main()
