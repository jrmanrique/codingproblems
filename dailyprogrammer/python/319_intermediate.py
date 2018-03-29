# https://www.reddit.com/r/dailyprogrammer/comments/6h9woe/20160614_challenge_319_intermediate_worm_wars_1/

def simulated(pop, seed, rate_table):
    def get_rates(rnd, rate_table):
        if len(rate_table.keys()) > 1:
            for t in sorted(rate_table.keys(), reverse=True):
                if rnd >= t:
                    return rate_table[t]
        return rate_table[0]

    s, i, r = pop - seed, seed, 0
    history = [[s], [i], [r]]
    rnd = 0
    while r < 0.99 * pop:
        rates = get_rates(rnd, rate_table)
        rnd += 1
        i = i + s * rates['si'] - i * rates['ir']
        r = r + s * rates['sr'] + i * rates['ir']
        s = pop - (i + r)
        for idx, x in enumerate([s, i, r]):
            history[idx].append(x)
    return history, len(history[0]) - 1


def randomized(pop, seed, rate_table, error=0.01):
    import random as rd

    def get_rates(rnd, rate_table):
        if len(rate_table.keys()) > 1:
            for t in sorted(rate_table.keys(), reverse=True):
                if rnd >= t:
                    return rate_table[t]
        return rate_table[0]

    s, i, r = pop - seed, seed, 0
    history = [[s], [i], [r]]
    rnd = 0
    while r < (1 - error) * pop:
        rates = get_rates(rnd, rate_table)
        rnd += 1
        for _ in range(s):
            if rd.random() < rates['si']:
                s -= 1
                i += 1
            elif rd.random() < rates['sr']:
                s -= 1
                r += 1
        for _ in range(i):
            if rd.random() < rates['ir']:
                i -= 1
                r += 1
        for idx, x in enumerate([s, i, r]):
            history[idx].append(x)
    return history, len(history[0]) - 1


def main():
    def plot(data, legend=None):
        import matplotlib.pyplot as plt

        plt.style.use('ggplot')
        for d in data:
            plt.plot(d)
        if legend:
            plt.legend(legend)
        plt.show()

    def clean(inp):
        inp = list(map(lambda x: x.strip(), inp.splitlines()))
        pop, seed = map(int, inp[0].split())
        rates = {}
        for t in inp[1:]:
            t = t.split()
            rates[int(t[0])] = {
                'si': float(t[1]),
                'ir': float(t[2]),
                'sr': float(t[3]),
            }
        return pop, seed, rates

    inp = """10000 10
    0 0.01 0.01 0.015
    100 0.02 0.01 0.015
    200 0.02 0.03 0.03"""

    mod, gens = randomized(*clean(inp), error=0.001)
    print('{} generations.'.format(gens))

    plot(mod, ['susceptible', 'infected', 'immune'])


if __name__ == '__main__':
    main()
