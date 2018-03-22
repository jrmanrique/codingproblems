# https://www.reddit.com/r/dailyprogrammer/comments/6nstip/20170717_challenge_324_easy_manual_square_root/

def long_division(num, prec):
    def split(s, n, from_right=False):
        if from_right:
            return [s[::-1][i:i + n][::-1] for i in range(0, len(s), 2)][::-1]
        else:
            return [s[i:i + n] for i in range(0, len(s), n)]

    def get_sq(num, buffer=0):
        return ((buffer * 20) + num) * num

    def get_maxsq(num, buffer=0):
        n = 1
        while get_sq(n, buffer=buffer) < num:
            n += 1
        return n - 1

    whole, dec = (str(num).split('.') + ['0'])[:2]

    dec += '0' * (prec * 2 - len(dec))
    dec = split(dec, 2)

    whole = '0' + whole if len(whole) % 2 else whole
    whole = split(whole, 2, from_right=True)

    sqrt = ''
    dividend = whole + dec
    for idx, w in enumerate(dividend):
        if idx == 0:
            n = int(w)
        else:
            n = int(''.join([dividend[idx - 1], w]))

        if sqrt:
            buff = int(sqrt)
        else:
            buff = 0

        msq = get_maxsq(n, buffer=buff)
        sqrt += str(msq)

        dividend[idx] = str(n - get_sq(msq, buffer=buff))

    lw = len(whole)
    if prec:
        return float(sqrt[:lw] + '.' + sqrt[lw:lw + prec])
    else:
        return int(sqrt[:lw])


def heros_method(num, prec):
    def _round(num, prec, down=True):
        from math import ceil, floor
        if down:
            return floor(num * (10 ** prec)) / (10 ** prec)
        else:
            return ceil(num * (10 ** prec)) / (10 ** prec)

    left = 0
    right = 1
    while left != right:
        left = right
        right = 0.5 * (right + (float(num) / right))

    if prec:
        return _round(right, prec)
    else:
        return int(right)


def main():
    inputs = [
        '0 7720.17',
        '1 7720.17',
        '2 7720.17',
        '0 12345',
        '8 123456',
        '1 12345678901234567890123456789',
    ]

    for inp in inputs:
        prec, num = inp.split()
        print('{} => {}'.format(num, heros_method(num, int(prec))))


if __name__ == '__main__':
    main()
