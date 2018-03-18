# https://www.reddit.com/r/dailyprogrammer/comments/7vm223/20180206_challenge_350_easy_bookshelf_problem/

def input_case(file=None):
    if file:
        with open(file, 'r') as f:
            contents = f.readlines()
        contents = list(map(lambda x: x.strip('\n'), contents))
        h, c = contents[0], contents[1:]
        on_sale = list(map(int, h.split()))
        books = [(int(x.split()[0]), ' '.join(x.split()[1:])) for x in c]
    else:
        on_sale = list(map(int, input().split()))

        books = []
        while True:
            x = input().split()
            if x:
                width = int(x[0])
                book = ' '.join(x[1:])
                books.append((width, book))
            else:
                break

    return on_sale, books


def allocate(shelves, books):
    sh = [[i, [], i] for i in sorted(shelves, reverse=True)]
    bo = [[i, False] for i in sorted(books, key=lambda x: x[0], reverse=True)]

    for book in bo:
        for shelf in sh:
            if book[0][0] <= shelf[2] and  not book[1]:
                shelf[1].append(book[0][1])
                shelf[2] -= book[0][0]
                book[1] = True
                break

    unfit = [i[0] for i in bo if not i[1]]
    sold = [shelf[:2] for shelf in sh if shelf[1]]
    return unfit, sold


def main():
    case = input_case(file='inputs/350_easy.in')
    unfit, sold = allocate(*case)
    if unfit:
        print('Impossible.')
        for book in unfit:
            print('{}: {}'.format(*book))
    else:
        print('{} shel{}'.format(len(sold), 'f' if len(sold) == 1 else 'ves'))
        for shelf in sold:
            print('{}: {}'.format(shelf[0], shelf[1]))


if __name__ == '__main__':
    main()
