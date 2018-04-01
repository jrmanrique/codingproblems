# https://projecteuler.net/problem=206

def match(num):
    return all([str(num)[i * 2] == str(i + 1) for i in range(9)])


def main():
    start = int(19293949596979899 ** 0.5) + 1
    for n in range(start, 0, -2):
        if match(n ** 2):
            print(n * 10)
            break


if __name__ == '__main__':
    main()
