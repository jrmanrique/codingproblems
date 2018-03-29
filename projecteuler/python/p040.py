# https://projecteuler.net/problem=40

def generate_string(length):
    i = 1
    out = ''
    while len(out) < length:
        out += str(i)
        i += 1
    return out


def main():
    text = generate_string(10 ** 6)
    sol = 1
    for e in range(6 + 1):
        sol *= int(text[10 ** e - 1])
    print(sol)


if __name__ == '__main__':
    main()
