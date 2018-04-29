"""Given a list of numbers, return whether any two sums to k.

For example, given [10, 15, 3, 7] and k of 17, return true since
10 + 7 is 17.

Bonus: Can you do this in one pass?
"""

import random as rd


def match(k, nums):
    watch = set()
    for num in nums:
        if num in watch:
            return True
        else:
            watch.add(k - num)
    return False


def generate_random(k, length=None):
    if length is None:
        length = optimal_length(k)
    return '{!s} {}'.format(k, ' '.join(map(str, [round(k * rd.random()) for _ in range(length)])))


def optimal_length(k, threshold=0.5, reps=100):
    for length in range(1, k + 1):
        count = 0
        for _ in range(reps):
            inp = generate_random(k, length)
            k, *nums = map(int, inp.split())
            if match(k, nums):
                count += 1
        if count / reps > threshold:
            return length
    return k


def main():
    inputs = [
        '17 10 15 3 7',
        generate_random(0, 0),
        generate_random(rd.randint(1, 50)),
        generate_random(rd.randint(1, 1000)),
    ]

    for inp in inputs:
        k, *nums = map(int, inp.split())
        print('{} {} => {}'.format(k, nums, match(k, nums)))


def bonus():
    """
    Show the probability of matching for every k, given a specific length.
    """

    import matplotlib.pyplot as plt

    reps = 1000
    max_k = 100
    length = 10

    data = []
    for k in range(1, max_k + 1):
        count = 0
        for _ in range(reps):
            inp = generate_random(k, length)
            k, *nums = map(int, inp.split())
            if match(k, nums):
                count += 1
        data.append(count / reps)

    plt.style.use('ggplot')
    plt.plot(data)
    plt.ylim(0, 1 * 1.05)
    plt.show()


if __name__ == '__main__':
    main()
    # bonus()
