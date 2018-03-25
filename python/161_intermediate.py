# https://www.reddit.com/r/dailyprogrammer/comments/24ypno/572014_challenge_161_medium_appointing_workers/

def input_case(file):
    with open(file, 'r') as f:
        inp = f.read()

    inp = list(map(lambda x: x.strip(), inp.splitlines()))
    lines = int(inp[0])
    people = [(x[0], x[1].split(',')) for x in map(lambda x: x.split(), inp[lines + 1:])]
    return inp[1:lines + 1], sorted(people, key=lambda x: len(x[1]))


def assign(work, people):
    def _assign(work, people):
        assigned = dict([(x, None) for x in work])
        for p in people:
            person, skills = p
            for skill in skills:
                if assigned[skill] is None:
                    assigned[skill] = person
                    break
        return assigned, set([x[0] for x in people]) - set(assigned.values())

    people = sorted(people, key=lambda x: len(x[1]))

    assigned, idle = _assign(work, people)
    while [w for w in assigned if assigned[w] is None]:
        for i in idle:
            u = people.pop([x[0] for x in people].index(i))
            people.insert(0, u)
        assigned, idle = _assign(work, people)

    return assigned, idle


def main():
    work, people = input_case('inputs/161_intermediate.in')

    assigned, idle = assign(work, people)

    for w in work:
        print(assigned[w], w)
    print(*idle, sep='\n')


if __name__ == '__main__':
    main()
