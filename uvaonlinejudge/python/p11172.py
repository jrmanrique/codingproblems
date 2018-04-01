# Relational Operator

def main():
    t = int(input())
    for _ in range(t):
        inp = input()
        a, b = [int(d) for d in inp.split()]
        if a > b:
            print('>')
        elif a < b:
            print('<')
        elif a == b:
            print('=')


if __name__ == '__main__':
    main()
