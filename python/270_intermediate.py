# https://www.reddit.com/r/dailyprogrammer/comments/4n6hc2/20160608_challenge_270_intermediate_generating/

from collections import defaultdict


def generate(text, step, length):
    import random as rd

    def build_table(text, step):
        words = text.split()
        table = defaultdict(list)

        for i in range(len(words) - step):
            table[tuple(words[i:i + step])].append(words[i + step])

        return table

    table = build_table(text, step)

    seed = rd.choice([s for s in table.keys() if s[0].isupper()])
    out = list(seed)

    for _ in range(length):
        out.append(rd.choice(table[tuple(out[-step:])]))

    return ' '.join(out)


def main():
    with open('inputs/270_intermediate.in', 'r') as f:
        inp = f.read().replace('\n', ' ')

    print(generate(inp, 5, 150))


if __name__ == '__main__':
    main()
