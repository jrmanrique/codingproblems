# https://www.reddit.com/r/dailyprogrammer/comments/7xkhar/20180214_challenge_351_intermediate_permutation/

def input_case(file=None):
    if file:
        with open(file, 'r') as f:
            contents = f.readlines()
        contents = list(map(lambda x: x.strip('\n'), contents))
        t, c = int(contents[0]), contents[1:]
        tests = [c[i * 2:2 * (i + 1)] for i in range(t)]
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
