# https://www.reddit.com/r/dailyprogrammer/comments/4gqm90/20160427_challenge_264_intermediate_gossiping_bus/?utm_term=e6fd0f95-43ce-413f-a2ed-35e98bd41c28&utm_medium=search&utm_source=reddit&utm_name=dailyprogrammer&utm_content=77

from collections import OrderedDict as dict


def any_dupes(seq):
    dupes = []
    for item in set(seq):
        dupes.append(tuple([i for i, x in enumerate(seq) if x == item]))
    return list(filter(lambda x: len(x) > 1, dupes))


def is_all(seq):
    keys = set(seq.keys())
    for v in seq.values():
        if v != keys:
            return False
    return True


def main():
    with open('inputs/264_intermediate.in', 'r') as f:
        inp = f.read()

    inp = list(map(lambda line: list(map(int, line.strip().split())), inp.splitlines()))

    drivers = dict([(d, set([d])) for d in range(len(inp))])

    for t in range(8 * 60):
        stops = [inp[d][t % len(inp[d])] for d in drivers.keys()]

        if any_dupes(stops):
            for dupe in any_dupes(stops):
                pool = set()
                for d in dupe:
                    pool |= drivers[d]
                for d in dupe:
                    drivers[d] |= pool

        if is_all(drivers):
            print(t, 'minutes')
            break
    else:
        print('never')


if __name__ == '__main__':
    main()
