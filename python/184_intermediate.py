# https://www.reddit.com/r/dailyprogrammer/comments/2jcgej/10152014_challenge_184_intermediate_radioactive/

from collections import OrderedDict as dict


def cycler(passes, rates, order):
    def cycle(pop, rates, order):
        old = [pop[i] for i in order]
        new = [0] * (len(order) + 1)
        for idx, elem in enumerate(order):
            new[idx] += old[idx] * (1 - rates[elem])
            new[idx + 1] += old[idx] * rates[elem]
        return dict(zip(order, new))


    history = dict([(i, []) for i in rates.keys()])
    pop = dict([(order[0], 100)] + [(i, 0) for i in order[1:]])
    for _ in range(passes):
        pop = cycle(pop, rates, order)
        for i in history.keys():
            history[i].append(pop[i])
    return pop, history


def randomizer(passes, rates, order):
    import random as rnd

    def progress_bar(completion, prefix='Progress:', suffix='Complete', decimals=1, bar_length=50):
        str_format = '{0:.' + str(decimals) + 'f}'
        percents = str_format.format(100 * completion)
        filled_length = int(round(bar_length * completion))
        bars = '█' * filled_length + '-' * (bar_length - filled_length)
        print('{} |{}| {}% {}'.format(prefix, bars, percents, suffix), end='\r')


    history = dict([(order[0], [10000])] + [(i, [0]) for i in order[1:]])
    working = [history[k][-1] for k in order]
    for p in range(passes):
        progress_bar(p / passes)

        for i, k in enumerate(working[:-1]):
            for _ in range(k):
                if rnd.random() < rates[order[i]]:
                    working[i] -= 1
                    working[i + 1] += 1

        for i, k in enumerate(order):
            history[k] += [working[i]]

    return dict(zip(order, working)), history


def main():
    def plot(data):
        import matplotlib.pyplot as plt

        plt.style.use('ggplot')
        for d in data.items():
            plt.plot(d[1], label=d[0])
        plt.legend()
        plt.show()


    inp = """50000
    a->b->c->d->s
    a: 0.00007
    b: 0.0005
    c: 0.00013
    d: 0.00022
    s: 0"""

    inp = list(map(lambda x: x.strip(), inp.splitlines()))
    t = int(inp[0])
    order = inp[1].split('->')
    rates = dict(zip(order, map(lambda x: float(x.split()[1]), inp[2:])))

    pop, history = randomizer(t, rates, order)
    print(pop)
    plot(history)


if __name__ == '__main__':
    main()
