import functools
import itertools
import sys

from util import expected_for_day

DAY = sys.argv[0].split(".")[0]

with open(f"{DAY}/input.txt") as fin:
    lines_in = fin.read().strip().split("\n")


def flatten(list_of_lists):
    """Flatten a list of lists to a list"""
    # flatten([[1, 2, 3], [11, 22, 33]]) --> [1, 2, 3, 11, 22, 33]
    return [x for xs in list_of_lists for x in xs]


def transpose(matrix):
    """Swap the rows and columns of a 2-D matrix."""
    # transpose([(1, 2, 3), (11, 22, 33)]) --> (1, 11) (2, 22) (3, 33)
    return zip(*matrix, strict=True)


def expanded_universe(matrix, factor):
    # Expand lines for cosmic expansion
    lines = flatten(
        [[line] if "#" in line else itertools.repeat(line, factor) for line in matrix]
    )
    # Expand cols for cosmic expansion
    cols = flatten(
        [
            [col] if "#" in col else itertools.repeat(col, factor)
            for col in transpose(lines)
        ]
    )
    return transpose(cols)


def galaxy_coords(matrix):
    return [
        (x, y)
        for y, line in enumerate(matrix)
        for x, col in enumerate(line)
        if col == "#"
    ]


def distance(pair):
    (x1, y1), (x2, y2) = pair
    return abs(x2 - x1) + abs(y2 - y1)


def get_distances_p1(lines, expansion_factor):
    matrix = expanded_universe(lines, expansion_factor)
    galaxies = galaxy_coords(matrix)
    pairs = itertools.combinations(galaxies, 2)
    return map(distance, pairs)


def universe_pos_y(lines, expansion, y):
    return functools.reduce(
        lambda acc, line: expansion - 1 + acc if "#" not in line else acc,
        list(lines)[:y],
        y,
    )


def universe_pos_x(lines, expansion, x):
    return universe_pos_y(transpose(lines), expansion, x)


def convert_position(lines, expansion, position):
    x, y = position
    return universe_pos_x(lines, expansion, x), universe_pos_y(lines, expansion, y)


def get_distances_p2(lines, expansion_factor):
    galaxies = list(
        map(
            lambda p: convert_position(lines, expansion_factor, p),
            galaxy_coords(lines),
        )
    )
    pairs = itertools.combinations(galaxies, 2)
    return map(distance, pairs)


p1_result = sum(get_distances_p1(lines_in, 2))
p2_result = sum(get_distances_p2(lines_in, 1000000))

p1_expected, p2_expected = expected_for_day(DAY)
assert p1_result == p1_expected
assert p2_result == p2_expected
print(f"{DAY} Part 1:", p1_result)
print(f"{DAY} Part 2:", p2_result)
