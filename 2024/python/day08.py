import sys
from collections import defaultdict
from itertools import combinations

from util import expected_for_day

DAY = sys.argv[0].split("/")[-1].split(".")[0]


with open(f"data/{DAY}/input.txt", "r") as file:
    ANTENNAS = defaultdict(list)
    grid = [(c, x, y) for y, r in enumerate(file) for x, c in enumerate(r.strip())]
    last_cxy = grid[-1]
    assert last_cxy[1] == last_cxy[2], "last x & y should match for a square grid"
    MAX = last_cxy[1]
    {ANTENNAS[c].append((x, y)) for c, x, y in grid if c != "."}


def in_grid(point):
    return (
        0 <= point[0] <= MAX
        and 0 <= point[0] <= MAX
        and 0 <= point[1] <= MAX
        and 0 <= point[1] <= MAX
    )


def solve(antennas, part_2=False):
    antinodes = set()

    for coords in antennas.values():
        for (start_y, start_x), (end_y, end_x) in combinations(coords, 2):
            dy = start_y - end_y
            dx = start_x - end_x

            if part_2:
                aa = (start_x, start_y)
                i = 1
                while in_grid(aa):
                    antinodes.add(aa)
                    aa = (start_x + dx * i, start_y + dy * i)
                    i += 1
                bb = (end_x, end_y)
                j = 1
                while in_grid(bb):
                    antinodes.add(bb)
                    bb = (end_x - dx * j, end_y - dy * j)
                    j += 1
            else:
                aa = (start_x + dx, start_y + dy)
                bb = (end_x - dx, end_y - dy)
                if in_grid(aa):
                    antinodes.add(aa)
                if in_grid(bb):
                    antinodes.add(bb)

    return len(antinodes)


p1_result = solve(ANTENNAS)
p2_result = solve(ANTENNAS, True)

p1_expected, p2_expected = expected_for_day(DAY)
assert p1_result == p1_expected
assert p2_result == p2_expected
print(f"{DAY} Part 1: {p1_result}")
print(f"{DAY} Part 2: {p2_result}")
