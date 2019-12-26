import sys


def day_3():
    def get_input():
        return [i.split(',') for i in sys.stdin.read().split('\n') if i]

    def get_points(wire):
        DIRECTIONS = {
            'U': (0, 1),
            'D': (0, -1),
            'L': (-1, 0),
            'R': (1, 0),
        }

        cx, cy, step = 0, 0, 0
        coords = {}
        for direct, moves in ((inst[:1], int(inst[1:])) for inst in wire):
            for _ in range(moves):
                cx += DIRECTIONS[direct][0]
                cy += DIRECTIONS[direct][1]
                step += 1
                coords[(cx, cy)] = step
        return coords

    wire_a, wire_b = get_input()

    a_path = get_points(wire_a)
    b_path = get_points(wire_b)
    intersections = [pt for pt in a_path if pt in b_path]

    return min(abs(x) + abs(y) for x, y in intersections)  # Part 1
    return min(a_path[pt] + b_path[pt] for pt in intersections)  # Part 2


if __name__ == "__main__":
    print('[OUT]', day_3())
