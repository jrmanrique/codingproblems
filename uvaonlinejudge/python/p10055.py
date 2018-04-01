# Hashmat the Brave Warrior

def main():
    while True:
        try:
            inp = input()
        except EOFError:
            break
        else:
            a, b = [int(d) for d in inp.split()]
            print(abs(b - a))


if __name__ == '__main__':
    main()
