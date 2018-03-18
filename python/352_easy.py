# https://www.reddit.com/r/dailyprogrammer/comments/7yyt8e/20180220_challenge_352_easy_making_imgurstyle/

def input_case():
    t = int(input())
    tests = []
    for _ in range(t):
        n = int(input())
        tests.append(n)
    return tests


def base62(num):
    ALPHABET = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    conv = ''
    while num // 62 != 0:
        num, idx = divmod(num, 62)
        conv += ALPHABET[idx]
    conv += ALPHABET[num]
    return ''.join(reversed(conv))


def main():
    cases = input_case()
    for case in cases:
        print('{} => {}'.format(case, base62(case)))


if __name__ == '__main__':
    main()
