import sys

from util import expected_for_day

DAY = sys.argv[0].split(".")[0]

with open(f"{DAY}/input.txt") as fin:
    lines_in = fin.read().strip().split("\n")


def transpose(matrix):
    """Swap the rows and columns of a 2-D matrix."""
    # transpose([(1, 2, 3), (11, 22, 33)]) --> (1, 11) (2, 22) (3, 33)
    return list(map("".join, zip(*matrix)))


def order_grid(grid, reverse):
    return [
        "#".join(
            ["".join(sorted(list(group), reverse=reverse)) for group in row.split("#")]
        )
        for row in grid
    ]


def tilt_north(grid):
    return transpose(order_grid(transpose(grid), True))


def tilt_west(grid):
    return order_grid(grid, True)


def tilt_east(grid):
    return order_grid(grid, False)


def tilt_south(grid):
    return transpose(order_grid(transpose(grid), False))


def cycle(grid):
    return tilt_east(tilt_south(tilt_west(tilt_north(grid))))


def total_load(grid):
    return sum(row.count("O") * (len(grid) - r) for r, row in enumerate(grid))


def part_1(lines):
    return total_load(tilt_north(lines))


def repeating_grid_list_with_start_offset(lines):
    result = tuple(lines)
    seen = {result}
    grids = [result]
    i = 0

    while True:
        i += 1
        result = tuple(cycle(result))
        if result in seen:
            break
        seen.add(result)
        grids.append(result)

    start = grids.index(result)
    return start, grids


def part_2(lines):
    total_cycles = 10**9
    start, grids = repeating_grid_list_with_start_offset(lines)
    answer_index = (total_cycles - start) % (len(grids) - start) + start
    return total_load(grids[answer_index])


p1_result = part_1(lines_in)
p2_result = part_2(lines_in)

p1_expected, p2_expected = expected_for_day(DAY)
assert p1_result == p1_expected
assert p2_result == p2_expected
print(f"{DAY} Part 1: {p1_result}")
print(f"{DAY} Part 2: {p2_result}")
