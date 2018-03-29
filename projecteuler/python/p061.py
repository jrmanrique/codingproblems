# https://projecteuler.net/problem=61

def quadratic(a, b, c):
    det = (b ** 2 - 4 * a * c) ** 0.5
    return ((-b - det) / (2 * a)), ((-b + det) / (2 * a))


def identify(num):
    def _istriangle(num):
        _, b = quadratic(1, 1, -2 * num)
        if b > 0 and b % 1 == 0:
            return True
        return False

    def _issquare(num):
        return pow(num, 0.5) % 1 == 0

    def _ispentagonal(num):
        _, b = quadratic(3, -1, -2 * num)
        if b > 0 and b % 1 == 0:
            return True
        return False

    def _ishexagonal(num):
        _, b = quadratic(2, -1, -num)
        if b > 0 and b % 1 == 0:
            return True
        return False

    def _isheptagonal(num):
        _, b = quadratic(5, -3, -2 * num)
        if b > 0 and b % 1 == 0:
            return True
        return False

    def _isoctagonal(num):
        _, b = quadratic(3, -2, -num)
        if b > 0 and b % 1 == 0:
            return True
        return False

    properties = set()
    if _istriangle(num):
        properties.add(3)
    if _issquare(num):
        properties.add(4)
    if _ispentagonal(num):
        properties.add(5)
    if _ishexagonal(num):
        properties.add(6)
    if _isheptagonal(num):
        properties.add(7)
    if _isoctagonal(num):
        properties.add(8)

    return properties


def check(seq):
    assign = {k: None for k in range(3, 8 + 1)}
    props = sorted([(num, identify(num)) for num in seq], key=lambda x: len(x[1]))
    for num, prop in props:
        for p in prop:
            if assign[p] is None:
                assign[p] = num
                break
    return sum([1 for i in assign.values() if i])


def main():
    from time import sleep


    seq = []
    for i in range(1000, 9999 + 1):
        if identify(i):
            seq.append(i)

    def isconnected(a, b):
        if str(b).startswith(str(a)[-2:]):
            return True
        return False

    length = 6
    stack = [[n, []] for n in seq]
    while stack:
        num, path = stack.pop()
        if len(path) >= length:
            if check(path) == length:
                print(path)
            continue
        if len(path) < length - 2:
            for child in [n for n in seq if isconnected(num, n)]:
                stack.append([child, path + [num]])
        else:
            nxt = int(str(num)[-2:] + str(path[0])[:2])
            if nxt in seq:
                stack.append([nxt, path + [num, nxt]])


def test():
    seq = []
    for i in range(1000, 9999 + 1):
        if identify(i):
            seq.append(i)

    test = [8256, 5625, 2512, 1281, 8128, 2882]
    for num in test:
        print(num, 'IN SEQ:', num in seq)
    print('ASSIGNED:', check(test))
    print('SUM:', sum(test))


if __name__ == '__main__':
    main()
    test()
