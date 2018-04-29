"""cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns
the first and last element of that pair. For example, car(cons(3, 4))
returns 3, and cdr(cons(3, 4)) returns 4.

Given this implementation of cons:

def cons(a, b):
    return lambda f : f(a, b)

Implement car and cdr.
"""

# Explanation: https://stackoverflow.com/questions/21769348/use-of-lambda-for-cons-car-cdr-definition-in-sicp

def cons(a, b):
    return lambda f: f(a, b)


def car(cons):
    return cons(lambda a, b: a)


def cdr(cons):
    return cons(lambda a, b: b)


def main():
    print('car(cons(3, 4)) == 3:', car(cons(3, 4)) == 3)
    print('cdr(cons(3, 4)) == 4:', cdr(cons(3, 4)) == 4)

    # [STEP BY STEP SOLUTION]

    # cons(3, 4) == lambda f: f(3, 4)

    # (lambda f: f(3, 4))(f) == 3
    # f(3, 4) == 3
    # f == (lambda a, b: a)

    # (lambda a, b: a)(3, 4) == 3
    # f(3, 4) == 3

    # (lambda f: f(3, 4))(lambda a, b: a) == 3
    # (cons(3, 4))(lambda a, b: a) == 3
    # car(cons(3, 4)) == 3

    # car(cons(3, 4)) == (cons(3, 4))(lambda a, b: a)


if __name__ == '__main__':
    main()
