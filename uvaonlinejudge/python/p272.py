# TEX Quotes

def main():
    counter = 0
    while True:
        try:
            inp = input()
        except EOFError:
            break
        else:
            line = ''
            for char in inp:
                if char == '"':
                    counter += 1
                    if counter % 2:
                        line += '``'
                    else:
                        line += '\'\''
                else:
                    line += char
        print(line)


if __name__ == '__main__':
    main()
