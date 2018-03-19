# https://www.reddit.com/r/dailyprogrammer/comments/6k123x/20170629_challenge_321_intermediate_affine_cipher/

def decode(a, b, word, retain_case=True):
    ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

    ciphertext = ''
    for char in word:
        if char.lower() in ALPHABET:
            cipherchar = ALPHABET[(a * ALPHABET.index(char.lower()) + b) % 26]
            if char.isupper() and retain_case:
                cipherchar = cipherchar.upper()
            ciphertext += cipherchar
        else:
            ciphertext += char

    return ciphertext


def get_valid_words(file):
    with open(file, 'r') as f:
        mapping = set(map(lambda x: x.lower().strip(), f.read().splitlines()))
        mapping |= set(['i', 'a'])
    return mapping


def solver(word, mapping):
    VALID_A = [3, 5, 7, 11, 15, 17, 19, 21, 23, 25]

    decoded = []
    for a in VALID_A:
        for b in range(26):
            s = decode(a, b, word)
            decoded.append((s, len([w for w in s.split() if w.lower() in mapping])))

    best = sorted(decoded, key=lambda x: x[1], reverse=True)
    top = [s for s in best if s[1] == best[0][1]]

    return [s[0] for s in top]


def main():
    words = [
        'NLWC WC M NECN',
        'YEQ LKCV BDK XCGK EZ BDK UEXLVM QPLQGWSKMB',
        'Yeq lkcv bdk xcgk ez bdk uexlv\'m qplqgwskmb.',
        'NH WRTEQ TFWRX TGY T YEZVXH GJNMGRXX STPGX NH XRGXR TX QWZJDW ZK WRNUZFB P WTY YEJGB ZE RNSQPRY XZNR YJUU ZSPTQR QZ QWR YETPGX ZGR NPGJQR STXQ TGY URQWR VTEYX WTY XJGB',
        'Nh wrteq tfwrx, tgy t yezvxh gjnmgrxx stpgx / Nh xrgxr, tx qwzjdw zk wrnuzfb p wty yejgb, / Ze rnsqpry xznr yjuu zsptqr qz qwr yetpgx / Zgr npgjqr stxq, tgy Urqwr-vteyx wty xjgb.',
    ]

    mapping = get_valid_words('inputs/321_intermediate.in')
    for word in words:
        print(solver(word, mapping))


if __name__ == '__main__':
    main()
