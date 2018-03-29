# BASE NEGATIVE

def to_decimal(n, base):
    digits = [int(d) for d in str(abs(n))]
    if n < 0:
        digits[0] *= -1
    mults = [base ** p for p in range(len(digits) - 1, -1, -1)]
    return sum([i[0] * i[1] for i in zip(mults, digits)])


def from_decimal(n, base):
    CHARMAP = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    flag = True if n < 0 else False
    n = abs(n)

    conv = []
    while n:
        n, d = divmod(n, base)
        conv.insert(0, d)

    num = ''.join([CHARMAP[:abs(base)][i] for i in conv])
    if flag:
        num = '-' + num
    return num


def invert_base(n, base):
    return from_decimal(to_decimal(n, base), -base)


def main():
    inputs = [
        '-10 7211',
        '-4 1302201',
        '-10 12345678',
        '-7 4021553',
        # '7 4016423',
        # '6 -3014515',
    ]

    for inp in inputs:
        r, n = list(map(int, inp.split()))
        print('{} {} => {}'.format(r, n, invert_base(n, r)))


if __name__ == '__main__':
    main()
