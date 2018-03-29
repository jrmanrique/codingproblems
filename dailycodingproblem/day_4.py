def main():
    inputs = [
        '3 4 -1 1',
        '1 2 0',
    ]

    for inp in inputs:
        inp = sorted([int(d) for d in inp.split()])
        expected = 1
        for d in inp:
            if d > 0:
                if d == expected:
                    expected += 1
                else:
                    break
        print('{} => {}'.format(inp, expected))



if __name__ == '__main__':
    main()
