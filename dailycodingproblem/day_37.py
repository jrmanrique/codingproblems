"""The power set of a set is the set of all its subsets. Write a
function that, given a set, generates its power set.

For example, given the set {1, 2, 3}, it should return
{{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}.

You may also use a list or array to represent a set.
"""

def main():
    def get_powerset(seq):
        for i in range(1 << len(seq)):
            subset = []
            for j, item in enumerate(seq):
                if i & (1 << j) > 0:
                    subset.append(item)
            yield tuple(subset)


    inp = [1, 2, 3]
    print(list(get_powerset(inp)))


def bonus():
    def get_powerset(seq, min_length=0, max_length=None):
        from itertools import chain, combinations

        if max_length is None:
            max_length = len(seq)

        return chain.from_iterable([combinations(seq, r) for r in range(min_length, max_length + 1)])

    inp = [1, 2, 3]
    print(list(get_powerset(inp)))


if __name__ == '__main__':
    main()
    bonus()
