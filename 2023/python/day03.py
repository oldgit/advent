import sys

from util import expected_for_day

DAY = sys.argv[0].split("/")[-1].split(".")[0]

NUMBERS = []
SYMBOLS = []
GEAR_POS = []


def get_numbers_symbols_gears(y, line):
    number = ""
    number_start = None
    x = -1
    for x, c in enumerate(line):
        if c.isdigit():
            if not number:
                number_start = (x - 1, y - 1)
            number = number + c
        else:
            if c == "*":
                GEAR_POS.append((x, y))
            if c != ".":
                SYMBOLS.append((x, y))
            if number:
                NUMBERS.append((int(number), number_start, (x, y + 1)))
                number = ""
    if number:
        NUMBERS.append((int(number), number_start, (x, y + 1)))


def number_next_to_symbol(number):
    start = number[1]
    end = number[2]
    adjacent = False
    for symbol in SYMBOLS:
        adjacent = (start[0] <= symbol[0] <= end[0]) and (
            start[1] <= symbol[1] <= end[1]
        )
        if adjacent:
            break
    return adjacent


def gear_ratio_for_pos(pos):
    gears = []
    for n in NUMBERS:
        start = n[1]
        end = n[2]
        if (start[0] <= pos[0] <= end[0]) and (start[1] <= pos[1] <= end[1]):
            gears.append(n[0])
    return gears[0] * gears[1] if len(gears) == 2 else 0


with open(f"data/{DAY}/input.txt", "r") as file:
    for y_in, line_in in enumerate(file.read().splitlines()):
        get_numbers_symbols_gears(y_in, line_in)

part_numbers = [n[0] for n in NUMBERS if number_next_to_symbol(n)]
part_numbers_sum = sum(part_numbers)
total_ratios = 0
for gp in GEAR_POS:
    ratio = gear_ratio_for_pos(gp)
    total_ratios = total_ratios + ratio


p1_expected, p2_expected = expected_for_day(DAY)
assert part_numbers_sum == p1_expected
assert total_ratios == p2_expected
print(f"{DAY} Part 1: {part_numbers_sum}")
print(f"{DAY} Part 2: {total_ratios}")
