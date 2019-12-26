import sys

from itertools import product


def day_2():
    def _modify_intcode(intcode: list, noun: int, verb: int) -> list:
        data = intcode.copy()
        data[1:3] = noun, verb
        return data

    def _solve_intcode(intcode: list) -> list:
        pointer = 0
        while True:
            opcode = intcode[pointer]
            loc_a = intcode[pointer + 1]
            loc_b = intcode[pointer + 2]
            loc_c = intcode[pointer + 3]

            if opcode == 1:
                intcode[loc_c] = intcode[loc_a] + intcode[loc_b]
            elif opcode == 2:
                intcode[loc_c] = intcode[loc_a] * intcode[loc_b]
            elif opcode == 99:
                break
            else:
                print(f'[ERR] Unknown opcode encountered at position {pointer}: {intcode[pointer]}.')
                break

            pointer += 4

        return intcode

    PAYLOAD = [int(i) for i in input().split(',')]
    TARGET = 19690720

    for noun, verb in product(range(1, 100), repeat=2):
        output = _solve_intcode(_modify_intcode(PAYLOAD, noun, verb))[0]
        if output == TARGET:
            print(f'[INF] Solutions found: {noun}, {verb}.')
            break
    
    return 100 * noun + verb


if __name__ == "__main__":
    print('[OUT]', day_2())
