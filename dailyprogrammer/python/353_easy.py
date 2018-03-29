# https://www.reddit.com/r/dailyprogrammer/comments/826coe/20180305_challenge_353_easy_closest_string/

def input_case(file=None):
    if file:
        with open(file, 'r') as f:
            contents = f.readlines()
        contents = list(map(lambda x: x.strip('\n'), contents))
        t, c = int(contents[0]), contents[1:]
        tests = []
        while c:
            n = c.pop(0)
            sto = [c.pop(0) for _ in range(int(n))]
            tests.append(sto)
        tests = tests[:t]
    else:
        t = int(input())

        tests = []
        for _ in range(t):
            n = int(input())
            line = []
            for _ in range(n):
                x = input()
                line.append(x)
            tests.append(line)

    return tests


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
    cases = input_case('inputs/353_easy.in')
    for case in cases:
        center, _ = find_center(case)
        print(center)


if __name__ == '__main__':
    main()
