from math import log10


def load_file(file):
    with open(file) as f:
        data = f.read()
    return data


def deepflatten(seq):
    result = []
    for item in seq:
        if isinstance(item, (list, set, tuple)):
            result.extend(deepflatten(item))
        else:
            result.append(item)
    return result


def partition(seq, length):
    return [seq[i:i + length] for i in range(0, len(seq), length)]


def join(seq, sep=''):
    return sep.join(seq)


def ispalindrome(string):
    if len(string) <= 1:
        return True
    elif string[0] == string[-1]:
        return ispalindrome(string[1:-1])
    return False


def get_digits(num):
    return [int(d) for d in str(num)]


def lend(num):
    return int(log10(num)) + 1
