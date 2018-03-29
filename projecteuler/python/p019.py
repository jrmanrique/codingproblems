# https://projecteuler.net/problem=19

def day(day, month, year):
    from math import floor as flr

    x = year - 1 if month < 3 else year
    c, y = divmod(x, 100)
    d = day
    m = (month - 2) % 12

    return (d + flr(2.6 * m - 0.2) + y + flr(y / 4) + flr(c / 4) - 2 * c) % 7


def main():
    DAYS = {
        0: 'Sunday',
        1: 'Monday',
        2: 'Tuesday',
        3: 'Wednesday',
        4: 'Thursday',
        5: 'Friday',
        6: 'Saturday',
    }

    counter = 0
    for yr in range(1901, 2000 + 1):
        for mo in range(1, 12 + 1):
            if day(1, mo, yr) == 0:
                counter += 1
                print('{}: {}/{}/{}'.format(counter, 1, mo, yr))


if __name__ == '__main__':
    main()
