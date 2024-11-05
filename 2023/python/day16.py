import sys

from util import expected_for_day

DAY = sys.argv[0].split("/")[-1].split(".")[0]

with open(f"data/{DAY}/input.txt") as fin:
    grid = fin.read().strip().split("\n")


def process_light_rays(sr, sc, sdr, sdc):
    max_rows = len(grid)
    max_cols = len(grid[0])
    light_rays = [(sr, sc, sdr, sdc)]
    rays_in_cells = set()

    while len(light_rays) > 0:
        r, c, dr, dc = light_rays.pop(0)
        r += dr
        c += dc

        if r < 0 or r >= max_rows or c < 0 or c >= max_cols:
            continue

        ch = grid[r][c]

        # ray passes through cell, no direction change
        if ch == "." or (ch == "-" and dc != 0) or (ch == "|" and dr != 0):
            if (r, c, dr, dc) not in rays_in_cells:
                rays_in_cells.add((r, c, dr, dc))
                light_rays.append((r, c, dr, dc))
        # turn ray up
        elif ch == "/":
            dr, dc = -dc, -dr
            if (r, c, dr, dc) not in rays_in_cells:
                rays_in_cells.add((r, c, dr, dc))
                light_rays.append((r, c, dr, dc))
        # turn ray down
        elif ch == "\\":
            dr, dc = dc, dr
            if (r, c, dr, dc) not in rays_in_cells:
                rays_in_cells.add((r, c, dr, dc))
                light_rays.append((r, c, dr, dc))
        # split the ray in two
        else:
            for dr, dc in [(1, 0), (-1, 0)] if ch == "|" else [(0, 1), (0, -1)]:
                if (r, c, dr, dc) not in rays_in_cells:
                    rays_in_cells.add((r, c, dr, dc))
                    light_rays.append((r, c, dr, dc))

    energized = {(r, c) for (r, c, _, _) in rays_in_cells}
    return len(energized)


def part_1():
    # start ray in top left   r, c, dr, dc
    return process_light_rays(0, -1, 0, 1)


def part_2():
    max_val = 0
    max_rows = len(grid)
    max_cols = len(grid[0])

    for r in range(max_rows):
        max_val = max(max_val, process_light_rays(r, -1, 0, 1))
        max_val = max(max_val, process_light_rays(r, max_cols, 0, -1))

    for c in range(max_rows):
        max_val = max(max_val, process_light_rays(-1, c, 1, 0))
        max_val = max(max_val, process_light_rays(max_rows, c, -1, 0))

    return max_val


p1_result = part_1()
p2_result = part_2()

p1_expected, p2_expected = expected_for_day(DAY)
assert p1_result == p1_expected
assert p2_result == p2_expected
print(f"{DAY} Part 1: {p1_result}")
print(f"{DAY} Part 2: {p2_result}")
