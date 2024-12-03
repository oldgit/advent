import sys
from util import expected_for_day

DAY = sys.argv[0].split("/")[-1].split(".")[0]


with open(f"data/{DAY}/input.txt", "r") as file:
    GRID = []
    while ROW := file.readline():
        COLS = list(map(lambda x: int(x), ROW.strip().split()))
        GRID.append(COLS)


def is_safe(levels):
    inc = all(y > x for x, y in zip(levels, levels[1:]))
    dec = all(x > y for x, y in zip(levels, levels[1:]))
    result = inc or dec
    if result:
        for x, y in zip(levels, levels[1:]):
            diff = abs(y - x)
            result = 0 < diff < 4
            if not result:
                break
    return result


def solve(grid, is_part2=False):
    result = 0
    for levels in grid:
        if is_part2:
            if is_safe(levels) or any(
                # iterate levels list dropping each level which could be unsafe
                is_safe(levels[:i] + levels[i + 1 :])
                for i in range(len(levels))
            ):
                result += 1
        else:
            if is_safe(levels):
                result += 1
    return result


p1_result = solve(GRID)
p2_result = solve(GRID, True)

p1_expected, p2_expected = expected_for_day(DAY)
assert p1_result == p1_expected
assert p2_result == p2_expected
print(f"{DAY} Part 1: {p1_result}")
print(f"{DAY} Part 2: {p2_result}")
