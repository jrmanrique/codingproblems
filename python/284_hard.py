# https://www.reddit.com/r/dailyprogrammer/comments/545a7x/20160923_challenge_284_hard_winning_the_tournament/

def winners(mapping, n=1000000):
    import random as rd

    def get_skill(player):
        return mapping[player]['skill']

    def sim(mapping):
        seed = list(mapping.keys())
        while len(seed) > 1:
            rd.shuffle(seed)
            games = [seed[i:i + 2] for i in range(0, len(seed), 2)]
            seed = []
            for game in games:
                p1, p2 = game
                p1_chance = get_skill(p1) / (get_skill(p1) + get_skill(p2))
                winner = p1 if rd.random() < p1_chance else p2
                seed.append(winner)
        mapping[seed[0]]['wins'] += 1
        return mapping

    for i in range(n):
        mapping = sim(mapping)

    return {i: {'skill': get_skill(i), 'chance': mapping[i]['wins'] / n} for i in range (1, len(mapping) + 1)}


def main():
    inp = '5 10 13 88 45 21 79 9 56 21 90 55 17 35 85 34'

    inp = inp.split()
    board = {i + 1: {'skill': int(inp[i]), 'wins': 0} for i in range(len(inp))}

    sol = winners(board)
    for i in range(1, len(inp) + 1):
        print('{:>2}: {:.6f}'.format(sol[i]['skill'], sol[i]['chance']))


if __name__ == '__main__':
    main()
