import sys

from util import expected_for_day

DAY = sys.argv[0].split(".")[0]

with open(f"{DAY}/input.txt") as fin:
    lines = fin.read().strip().split("\n")

DIRS = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}


def trench_length_coords_p1():
    length = 0
    coords = [(0, 0)]
    for line in lines:
        d, n, _ = line.split()
        dr, dc = DIRS[d]
        n = int(n)
        length = length + n
        r, c = coords[-1]
        coords.append((r + dr * n, c + dc * n))
    return length, coords


def trench_length_coords_p2():
    length = 0
    coords = [(0, 0)]
    for line in lines:
        _, _, rgb_code = line.split()
        rgb_code = rgb_code[2:-1]
        dr, dc = DIRS["RDLU"[int(rgb_code[-1])]]
        n = int(rgb_code[:-1], 16)
        length = length + n
        r, c = coords[-1]
        coords.append((r + dr * n, c + dc * n))
    return length, coords


def area_enclosed_by_trench(coords):
    # Use Shoelace formula: https://en.wikipedia.org/wiki/Shoelace_formula
    # triangle form to calculate area of trench polygon
    return abs(
        sum(
            coords[i][0] * (coords[i - 1][1] - coords[(i + 1) % len(coords)][1])
            for i in range(len(coords))
        )
        // 2
    )


def interior_squares_count_from_trench_length(area, trench_length):
    # Use Pick's theorem: https://en.wikipedia.org/wiki/Pick's_theorem
    # i = A - b/2 + 1
    return area - (trench_length // 2) + 1


def calculate_area(length, coords):
    area = area_enclosed_by_trench(coords)
    interior_squares = interior_squares_count_from_trench_length(area, length)
    return interior_squares + length


def part_1():
    length, coords = trench_length_coords_p1()
    return calculate_area(length, coords)


def part_2():
    length, coords = trench_length_coords_p2()
    return calculate_area(length, coords)


p1_result = part_1()
p2_result = part_2()

p1_expected, p2_expected = expected_for_day(DAY)
assert p1_result == p1_expected
assert p2_result == p2_expected
print(f"{DAY} Part 1: {p1_result}")
print(f"{DAY} Part 2: {p2_result}")
