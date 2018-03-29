# https://projecteuler.net/problem=63

def main():
    counter = 0
    limit = 1000
    for p in range(1, limit):
        for n in range(1, limit):
            num = pow(n, p)
            if len(str(num)) == p:
                counter += 1
                print('{}^{} = {:,}'.format(n, p, num))
            elif len(str(num)) > p:
                break
    print('ANSWER:', counter)


if __name__ == '__main__':
    main()
