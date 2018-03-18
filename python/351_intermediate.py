# https://www.reddit.com/r/dailyprogrammer/comments/7xkhar/20180214_challenge_351_intermediate_permutation/

import svctools as svc


def input_case(file=None):
    if file:
        tests = svc.read_file(file, 2)
        tests = [[test[0], test[1].split(',')] for test in tests]
    else:
        t = int(input())
        tests = []
        for _ in range(t):
            progs = input()
            moves = input()
            tests.append((progs, moves.split(',')))
    return tests


def dance(programs, moves):
    progs = list(programs)
    for move in moves:
        key, value = move[:1], move[1:]

        if key == 's':
            value = int(value)
            progs = progs[-value:] + progs[:-value]
        elif key == 'x':
            a, b = list(map(int, value.split('/')))
            progs[a], progs[b] = progs[b], progs[a]
        elif key == 'p':
            a, b = list(map(int, value.split('/')))
            c = progs.index(programs[a])
            d = progs.index(programs[b])
            progs[c], progs[d] = progs[d], progs[c]
    return ''.join(progs)


def main():
    cases = input_case(file='inputs/351_intermediate.in')
    for _, case in enumerate(cases):
        print('{} => {}'.format(case[0], dance(*case)))


if __name__ == '__main__':
    main()
