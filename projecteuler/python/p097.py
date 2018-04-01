# https://projecteuler.net/problem=97

def main():
    num = 1
    for _ in range(7830457):
        num = (num * 2) % (10 ** 10)
    num = 28433 * num + 1
    print(str(num)[-10:])


if __name__ == '__main__':
    main()
