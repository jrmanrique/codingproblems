# https://www.reddit.com/r/dailyprogrammer/comments/826coe/20180305_challenge_353_easy_closest_string/

def input_case():
    n = int(input())

    lines = []
    for _ in range(n):
        line = input()
        lines.append(line)

    return lines


def list_pairs(lst):
    return [(row, lst[:idx] + lst[idx + 1:]) for idx, row in enumerate(lst)]


def compute_distance(target, partners):
    def hamming_distance(a, b):
        return sum([1 for i in range(len(a)) if a[i] != b[i]])

    counter = 0
    for partner in partners:
        counter += hamming_distance(target, partner)
    return counter


def find_center(lst):
    pairs = list_pairs(lst)
    dists = [(pair[0], compute_distance(pair[0], pair[1])) for pair in pairs]
    dists = sorted(dists, key=lambda x: x[1])
    mins = list(filter(lambda x: x[1] <= dists[0][1], dists))
    return [min[0] for min in mins], dists[0][1]


def main():
    case = input_case()
    center, _ = find_center(case)
    print(center)


if __name__ == '__main__':
    main()
