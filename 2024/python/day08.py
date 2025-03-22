import sys

from util import expected_for_day

DAY = sys.argv[0].split("/")[-1].split(".")[0]

with open(f"data/{DAY}/input.txt", "r") as file:
    GRID = file.read().strip().split("\n")
    MAX_ROWS = len(GRID)
    MAX_COLS = len(GRID[0])
    ANTENNA_MAP = {}
    for Y, r in enumerate(GRID):
        for X, c in enumerate(r):
            if c != ".":
                ls = ANTENNA_MAP.get(c, [])
                ls.append((X, Y))
                ANTENNA_MAP[c] = ls


def add_if_in_grid(anti_node_set, x, y):
    if 0 <= x < MAX_COLS and 0 <= y < MAX_ROWS:
        anti_node_set.add((x, y))


def solve(part_2=False):
    anti_nodes = set()
    for freq in ANTENNA_MAP.keys():
        antennas = ANTENNA_MAP.get(freq)
        for i in range(len(antennas)):
            for j in range(i + 1, len(antennas)):
                dx, dy = (
                    antennas[j][0] - antennas[i][0],
                    antennas[j][1] - antennas[i][1],
                )
                max_inc_distance = max(abs(dx), abs(dy))
                n = int(MAX_COLS / max_inc_distance) + 1 if part_2 else 2
                for k in range(1, n):
                    add_if_in_grid(
                        anti_nodes, antennas[i][0] - (k * dx), antennas[i][1] - (k * dy)
                    )
                    add_if_in_grid(
                        anti_nodes, antennas[j][0] + (k * dx), antennas[j][1] + (k * dy)
                    )
                if part_2:
                    anti_nodes.add(antennas[i])
                    anti_nodes.add(antennas[j])
    return len(anti_nodes)


p1_result = solve()
p2_result = solve(True)

p1_expected, p2_expected = expected_for_day(DAY)
assert p1_result == p1_expected
assert p2_result == p2_expected
print(f"{DAY} Part 1: {p1_result}")
print(f"{DAY} Part 2: {p2_result}")
