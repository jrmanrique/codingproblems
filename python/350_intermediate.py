# https://www.reddit.com/r/dailyprogrammer/comments/7vx85p/20180207_challenge_350_intermediate_balancing_my/


def input_case(file=None):
    if file:
        with open(file, 'r') as f:
            contents = f.readlines()
        contents = list(map(lambda x: x.strip('\n'), contents))
        t, c = int(contents[0]), contents[1:]
        tests = [c[i * 2:2 * (i + 1)] for i in range(t)]
        tests = [list(map(int, test[1].split()[:int(test[0])])) for test in tests]
    else:
        t = int(input())
        tests = []
        for _ in range(t):
            n = int(input())
            values = input()
            tests.append(list(map(int, values.split()[:n])))
    return tests


def balance(lst):
    return [i for i, _ in enumerate(lst) if sum(lst[:i]) == sum(lst[i + 1:])]


def main():
    cases = input_case(file='inputs/350_intermediate.in')
    for _, case in enumerate(cases):
        print('{} => {}'.format(case, balance(case)))


if __name__ == '__main__':
    main()
