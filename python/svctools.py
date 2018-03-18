from math import ceil


def read_file(file, lines, header=True):
    """
    Reads files and parses each line into test cases. Parameters:\n
    file: path to file (Str)\n
    lines: number of lines per test case (Int)\n
    header: first line is number of test cases if True (Bool)
    """

    with open(file, 'r') as f:
        contents = f.readlines()
    contents = list(map(lambda x: x.strip('\n'), contents))
    if header:
        t, c = int(contents[0]), contents[1:]
    else:
        t = ceil(len(contents) / lines)
        c = contents
    tests = [c[i * lines:lines * (i + 1)] for i in range(t)]
    return tests
