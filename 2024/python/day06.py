import sys
from util import expected_for_day

DAY = sys.argv[0].split("/")[-1].split(".")[0]

DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]


with open(f"data/{DAY}/input.txt", "r") as file:
    GRID = {(i, j): c for i, r in enumerate(file) for j, c in enumerate(r.strip())}
    START = [p for p in GRID if GRID[p] == "^"][0]


def next_step(d, y, x):
    dy, dx = DIRS[d]
    y, x = y + dy, x + dx
    return y, x


def walk(grid):
    pos, dirn, seen = START, 0, set()
    while pos in grid and (pos, dirn) not in seen:
        seen.add((pos, dirn))
        n = next_step(dirn, pos[0], pos[1])
        if grid.get(n) == "#":
            dirn = (dirn + 1) % 4
        else:
            pos = n
    positions = {p for p, _ in seen}
    is_loop = (pos, dirn) in seen
    return positions, is_loop


def part2(steps, grid):
    count = 0
    for s in steps:
        # set an obstruction at each guard step & see if it's a loop
        is_loop = walk(grid | {s: "#"})[1]
        if is_loop:
            count += 1
    return count


path = walk(GRID)[0]
p1_result = len(path)
p2_result = part2(path, GRID)

p1_expected, p2_expected = expected_for_day(DAY)
assert p1_result == p1_expected
assert p2_result == p2_expected
print(f"{DAY} Part 1: {p1_result}")
print(f"{DAY} Part 2: {p2_result}")
