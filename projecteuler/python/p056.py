def sumdig(num):
    return sum([int(d) for d in str(num)])


def main():
    best = (0, 0 ,0)
    for a in range(1, 100):
        for b in range(1, 100):
            ans = sumdig(pow(a, b))
            if ans > best[2]:
                best = (a, b, ans)

    print(best)


if __name__ == '__main__':
    main()
