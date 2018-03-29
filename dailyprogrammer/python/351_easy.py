# https://www.reddit.com/r/dailyprogrammer/comments/7x81yg/20180213_challenge_351_easy_cricket_scoring/

def input_case():
    t = int(input())
    tests = []
    for _ in range(t):
        n = input()
        tests.append(n)
    return tests


def score_cricket(tally):
    players = {i: 0 for i in range(1, 11 + 1)}
    on_strike, off_strike, next_player = [1, 2, 3]
    extras = 0
    over = 0
    for run in tally:
        if run.isdigit():
            players[on_strike] += int(run)
            if int(run) % 2:
                on_strike, off_strike = off_strike, on_strike
        elif run == '.':
            pass
        elif run == 'b':
            extras += 1
            on_strike, off_strike = off_strike, on_strike
        elif run == 'w':
            extras += 1
        elif run == 'W':
            if next_player <= 11:
                on_strike = next_player
                next_player += 1
            else:
                break

        if run == 'w':
            pass
        else:
            over += 1

        if over >= 6:
            over = 0
            on_strike, off_strike = off_strike, on_strike

    return players, extras


def main():
    cases = input_case()
    for idx, case in enumerate(cases):
        print('Case {}: {}'.format(idx + 1, case))
        players, extras = score_cricket(case)
        for player, runs in players.items():
            print('Player {}: {}'.format(player, runs))
        print('Extras:', extras)


if __name__ == '__main__':
    main()
