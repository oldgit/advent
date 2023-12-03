NUMBERS = []
SYMBOLS = []
GEAR_POS = []


def get_numbers_symbols_gears(y, line):
    number = ""
    number_start = None
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
        adjacent = (symbol[0] >= start[0] and symbol[0] <= end[0]) and (
            symbol[1] >= start[1] and symbol[1] <= end[1]
        )
        if adjacent:
            break
    return adjacent


def gear_ratio_for_pos(pos):
    gears = []
    for n in NUMBERS:
        start = n[1]
        end = n[2]
        if (pos[0] >= start[0] and pos[0] <= end[0]) and (
            pos[1] >= start[1] and pos[1] <= end[1]
        ):
            gears.append(n[0])
    return gears[0] * gears[1] if len(gears) == 2 else 0


with open("day03/input.txt", "r") as file:
    for y, line in enumerate(file.read().splitlines()):
        get_numbers_symbols_gears(y, line)

part_numbers = [n[0] for n in NUMBERS if number_next_to_symbol(n)]
total_ratios = 0
for gp in GEAR_POS:
    ratio = gear_ratio_for_pos(gp)
    total_ratios = total_ratios + ratio

print("Part 1:", sum(part_numbers))
print("Part 2:", total_ratios)
