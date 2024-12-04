import sys
from util import expected_for_day

DAY = sys.argv[0].split("/")[-1].split(".")[0]


with open(f"data/{DAY}/input.txt", "r") as file:
    GRID = file.read().strip().split("\n")
    MAX_ROWS = len(GRID)
    MAX_COLS = len(GRID[0])


def inc_if_xmas(word, count):
    if word == "XMAS" or word == "SAMX":
        count += 1
    return count


def part1():
    count = 0
    for y in range(MAX_ROWS):
        for x in range(MAX_COLS):
            if y + 3 < MAX_ROWS:
                count = inc_if_xmas("".join(GRID[y + n][x] for n in range(4)), count)
            if x + 3 < MAX_COLS:
                count = inc_if_xmas("".join(GRID[y][x + n] for n in range(4)), count)
            if x + 3 < MAX_COLS and y + 3 < MAX_ROWS:
                count = inc_if_xmas(
                    "".join(GRID[y + n][x + n] for n in range(4)), count
                )
            if x - 3 >= 0 and y + 3 < MAX_ROWS:
                count = inc_if_xmas(
                    "".join(GRID[y + n][x - n] for n in range(4)), count
                )
    return count


def part2():
    count = 0
    for y in range(MAX_ROWS):
        for x in range(MAX_COLS):
            if 0 < x < (MAX_COLS - 1) and 0 < y < (MAX_ROWS - 1) and GRID[y][x] == "A":
                top = "".join(GRID[y - 1][x - 1] + GRID[y - 1][x + 1])
                bottom = "".join(GRID[y + 1][x - 1] + GRID[y + 1][x + 1])
                if (
                    (top == "MS" and bottom == "MS")
                    or (top == "SM" and bottom == "SM")
                    or (top == "SS" and bottom == "MM")
                    or (top == "MM" and bottom == "SS")
                ):
                    count += 1
    return count


p1_result = part1()
p2_result = part2()

p1_expected, p2_expected = expected_for_day(DAY)
assert p1_result == p1_expected
assert p2_result == p2_expected
print(f"{DAY} Part 1: {p1_result}")
print(f"{DAY} Part 2: {p2_result}")
