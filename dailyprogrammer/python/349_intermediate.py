# https://www.reddit.com/r/dailyprogrammer/comments/7ubc70/20180130_challenge_349_intermediate_packing/

def input_case(file=None):
    if file:
        with open(file, 'r') as f:
            contents = f.readlines()
        contents = list(map(lambda x: x.strip('\n'), contents))
        t, c = int(contents[0]), contents[1:]
        tests = [(int(i.split()[0]), [int(d) for d in i.split()[1]]) for i in c]
    else:
        t = int(input())
        tests = []
        for _ in range(t):
            i = input()
            tests.append((int(i.split()[0]), [int(d) for d in i.split()[1]]))
    return tests


def stack_boxes(rows, boxes):
    from itertools import accumulate, permutations

    def find(boxes, size):
        for case in permutations(boxes):
            s = sum(case)
            if s == size:
                return [case]
            for idx, n in enumerate(accumulate(case), 1):
                if s - n == size:
                    return [case[idx:]] + list(find(case[:idx], size))

    load, not_possible = divmod(sum(boxes), rows)

    if not_possible:
        return False
    return find(boxes, load)


def main():
    cases = input_case(file='inputs/349_intermediate.in')
    for idx, case in enumerate(cases):
        print('Case {}: {}'.format(idx, case))
        matrix = stack_boxes(*case)
        if matrix:
            print(*[''.join(list(map(str, row))) for row in matrix],sep='\n')
        else:
            print('Unstackable.')

if __name__ == '__main__':
    main()
