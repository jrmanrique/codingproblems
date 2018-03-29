# https://projecteuler.net/problem=17

def to_words(num):
    def chunker(num):
        chunks = []
        while num:
            num, tho = divmod(num, 1000)
            chunks.insert(0, tho)
        return chunks

    def name_hundreds(chunk):
        def isolate(chunk):
            return [int(i) for i in str(chunk).zfill(3)]

        ONES = {
            0: 'zero',
            1: 'one',
            2: 'two',
            3: 'three',
            4: 'four',
            5: 'five',
            6: 'six',
            7: 'seven',
            8: 'eight',
            9: 'nine',
        }
        TENS = {
            0: '',
            1: 'ten',
            2: 'twenty',
            3: 'thirty',
            4: 'forty',
            5: 'fifty',
            6: 'sixty',
            7: 'seventy',
            8: 'eighty',
            9: 'ninety',
        }
        TENONE = {
            1: 'eleven',
            2: 'twelve',
            3: 'thirteen',
            4: 'fourteen',
            5: 'fifteen',
            6: 'sixteen',
            7: 'seventeen',
            8: 'eighteen',
            9: 'nineteen',
        }

        hund, tens, ones = isolate(chunk)
        message = []
        if hund:
            message.insert(0, ONES[hund] + ' hundred')
            if tens or ones:
                message.insert(0, 'and')
        if tens:
            if tens == 1:
                if ones == 0:
                    message.insert(0, TENS[tens])
            else:
                message.insert(0, TENS[tens])
        if ones:
            if tens == 1:
                message.insert(0, TENONE[ones])
            else:
                message.insert(0, ONES[ones])
        return message

    def name_all(num):
        SEPS = {
            0: '',
            1: 'thousand',
            2: 'million',
            3: 'billion',
            4: 'trillion',
            5: 'quadrillion',
        }

        message = []
        for i, c in enumerate(chunker(num)[::-1]):
            message.append(SEPS[i])
            message.extend(name_hundreds(c))
        return message[::-1]

    return ' '.join(name_all(num)).strip()


def main():
    num = 1000

    counter = 0
    for n in range(1, num + 1):
        counter += len(''.join(to_words(n).split()))

    print(counter)


if __name__ == '__main__':
    main()
