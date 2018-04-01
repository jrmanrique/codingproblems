# Stacking Boxes

def load_file(file):
    with open(file) as f:
        data = f.read()
    return data


def load_input():
    inp = ''
    while True:
        try:
            line = input()
        except EOFError:
            break
        else:
            inp += line + '\n'
    return inp


def parse_input(string):
    inp = string.splitlines()

    cases = []
    while inp:
        n, dims = [int(d) for d in inp.pop(0).split()]
        case = [tuple([int(d) for d in ln.split()][:dims]) for ln in inp[:n]]
        cases.append(case)
        inp = inp[n:]

    return cases


def isfit(boxa, boxb):
    return all([a < b for a, b in zip(sorted(boxa), sorted(boxb))])


def find_path(boxes):
    best = []
    boxes = set(boxes)
    stack = [[[box], boxes - set(box)] for box in sorted(boxes, reverse=True)]
    while stack:
        path, remaining = stack.pop()
        if len(path) >= len(best):
            best = path
            if len(best) == len(boxes):
                return best
        for child in remaining:
            if isfit(path[-1], child):
                stack.append([path + [child], remaining - set(child)])
    return best


def main():
    inp = load_input()
    cases = parse_input(inp)

    for case in cases:
        solution = [case.index(box) + 1 for box in find_path(case)]
        print(len(solution))
        print(' '.join([str(d) for d in solution]))


if __name__ == '__main__':
    main()
