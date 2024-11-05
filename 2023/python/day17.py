import sys
from heapq import heappush, heappop

from util import expected_for_day

DAY = sys.argv[0].split("/")[-1].split(".")[0]

with open(f"data/{DAY}/input.txt") as fin:
    grid = [list(map(int, line.strip())) for line in fin.read().strip().split("\n")]


def lowest_heatloss_path(direction_min, direction_max):
    seen = set()
    max_r = len(grid) - 1
    max_c = len(grid[0]) - 1
    heat_loss = 0
    r = 0
    c = 0
    priority_queue = [(heat_loss, r, c, 0, 0, 0)]

    while True:
        heat_loss, r, c, dr, dc, n = heappop(priority_queue)

        if r == max_r and c == max_c and n >= direction_min:
            return heat_loss

        if (r, c, dr, dc, n) in seen:
            continue

        seen.add((r, c, dr, dc, n))

        if n < direction_max and (r, c) != (0, 0):
            nr = r + dr
            nc = c + dc
            if 0 <= nr <= max_r and 0 <= nc <= max_c:
                heappush(
                    priority_queue, (heat_loss + grid[nr][nc], nr, nc, dr, dc, n + 1)
                )

        if n >= direction_min or (r, c) == (0, 0):
            for ndr, ndc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                if (ndr, ndc) != (dr, dc) and (ndr, ndc) != (-dr, -dc):
                    nr = r + ndr
                    nc = c + ndc
                    if 0 <= nr <= max_r and 0 <= nc <= max_c:
                        heappush(
                            priority_queue,
                            (heat_loss + grid[nr][nc], nr, nc, ndr, ndc, 1),
                        )


def part_1():
    return lowest_heatloss_path(1, 3)


def part_2():
    return lowest_heatloss_path(4, 10)


p1_result = part_1()
p2_result = part_2()

p1_expected, p2_expected = expected_for_day(DAY)
assert p1_result == p1_expected
assert p2_result == p2_expected
print(f"{DAY} Part 1: {p1_result}")
print(f"{DAY} Part 2: {p2_result}")
