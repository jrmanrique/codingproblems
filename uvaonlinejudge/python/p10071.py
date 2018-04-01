# Back to High School Physics

def main():
    while True:
        try:
            inp = input()
        except EOFError:
            break
        else:
            v, t = [int(d) for d in inp.split()]
            print(2 * v * t)


if __name__ == '__main__':
    main()
