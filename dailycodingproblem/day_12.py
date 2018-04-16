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
