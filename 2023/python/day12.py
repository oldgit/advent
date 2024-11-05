import sys

from util import expected_for_day

DAY = sys.argv[0].split("/")[-1].split(".")[0]

CACHE = {}

with open(f"data/{DAY}/input.txt") as fin:
    lines_in = fin.read().strip().split("\n")


def count(layout, bnums):
    # recursion stop when layout or bnums is empty
    if layout == "":
        return 1 if bnums == () else 0
    if bnums == ():
        return 0 if "#" in layout else 1

    key = (layout, bnums)

    # repeated combo is fetched from cache
    if key in CACHE:
        return CACHE[key]

    result = 0

    if layout[0] in ".?":
        result += count(layout[1:], bnums)

    if layout[0] in "#?":
        if (
            bnums[0] <= len(layout)
            and "." not in layout[: bnums[0]]
            and (bnums[0] == len(layout) or layout[bnums[0]] != "#")
        ):
            result += count(layout[bnums[0] + 1 :], bnums[1:])

    CACHE[key] = result
    return result


def part_1(lines):
    total = 0
    for line in lines:
        layout, bnums = line.split()
        bnums = tuple(map(int, bnums.split(",")))
        total += count(layout, bnums)

    return total


def part_2(lines, copies):
    total = 0
    for line in lines:
        layout, bnums = line.split()
        bnums = tuple(map(int, bnums.split(",")))
        layout = "?".join([layout] * copies)
        bnums *= copies
        total += count(layout, bnums)

    return total


p1_result = part_1(lines_in)
p2_result = part_2(lines_in, 5)

p1_expected, p2_expected = expected_for_day(DAY)
assert p1_result == p1_expected
assert p2_result == p2_expected
print(f"{DAY} Part 1: {p1_result}")
print(f"{DAY} Part 2: {p2_result}")
