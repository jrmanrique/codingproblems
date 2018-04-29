"""There exists a staircase with N steps, and you can climb up either
1 or 2 steps at a time. Given N, write a function that returns the
number of unique ways you can climb the staircase. The order of the
steps matters.

For example, if N is 4, then there are 5 unique ways:
- 1, 1, 1, 1
- 2, 1, 1
- 1, 2, 1
- 1, 1, 2
- 2, 2

What if, instead of being able to climb 1 or 2 steps at a time, you
could climb any number from a set of positive integers X? For example,
if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.
"""

def get_steps(n, steps):
    ways = []
    stack = [[n, []]]
    while stack:
        rem, path = stack.pop()
        if rem == 0:
            ways.append(path)
            continue
        for step in filter(lambda x: x <= rem, steps):
            stack.append([rem - step, path + [step]])
    return ways


def main():
    n = int(input())
    steps = [int(d) for d in input().split()]

    if not steps:
        steps = [1, 2]

    ways = get_steps(n, steps)
    print(len(ways))


if __name__ == '__main__':
    main()
