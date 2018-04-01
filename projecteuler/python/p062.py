# https://projecteuler.net/problem=62

def largeperm(num):
    return int(''.join(sorted([d for d in str(num)], reverse=True)))


def main():
    n = 100

    found = False
    cache = {}
    while not found:
        smallperm = largeperm(n ** 3)
        if smallperm not in cache:
            cache[smallperm] = {'times': 1, 'perms': [n]}
        else:
            cache[smallperm]['times'] += 1
            cache[smallperm]['perms'] += [n]
        if cache[smallperm]['times'] == 5:
            found = True
            result = cache[smallperm]
        else:
            n += 1

    print(result['perms'])
    print('ANSWER:', min(result['perms']) ** 3)


if __name__ == '__main__':
    main()
