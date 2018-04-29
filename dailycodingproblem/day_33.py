"""Compute the running median of a sequence of numbers. That is, given
a stream of numbers, print out the median of the list so far on each
new element.

Recall that the median of an even-numbered list is the average of the
two middle numbers.
"""

def average(seq):
    return sum(seq) / len(seq)


def median(seq):
    seq = sorted(seq)
    middle = len(seq) // 2
    if len(seq) % 2:
        return seq[middle]
    return average(seq[middle - 1:middle + 1])


def running_median(seq):
    meds = []
    new = []
    for i, _ in enumerate(seq):
        new.append(seq[i])
        meds.append(median(new))
    return meds


def main():
    inp = [2, 1, 5, 7, 2, 0, 5]
    print('{} => {}'.format(inp, running_median(inp)))


if __name__ == '__main__':
    main()
