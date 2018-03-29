# https://projecteuler.net/problem=48

def main():
    print(str(sum([pow(i, i) for i in range(1, 1000 + 1)]))[-10:])


if __name__ == '__main__':
    main()
