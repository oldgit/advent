import sys
from collections import deque

from util import expected_for_day

DAY = sys.argv[0].split(".")[0]

DIRECTIONS = [(-1, 0), (1, 0), (0, 1), (0, -1)]

with open(f"{DAY}/input.txt") as fin:
    LINES = fin.read().strip().split("\n")

I_MAX, J_MAX = len(LINES), len(LINES[0])
assert I_MAX == J_MAX, f"Not a square grid: {I_MAX} x {J_MAX}"
GRID_SIZE = I_MAX
STEPS_TO_EDGE = I_MAX // 2

# Find starting point SI, SJ
SI, SJ = None, None
for INDEX, line in enumerate(LINES):
    if "S" in line:
        SI, SJ = INDEX, line.index("S")
        break
assert SI is not None
assert SJ is not None

#      queue( ((x, y), step_count) )
QUEUE: deque[tuple[tuple[int, int], int]] = deque()
#        dict( (x, y), step_count )
VISITED: dict[tuple[int, int], int] = {}


def take_step_from(si, sj, step_count):
    step_count += 1
    for di, dj in DIRECTIONS:
        i, j = si + di, sj + dj
        if (
            (i, j) not in VISITED
            and 0 <= i < I_MAX
            and 0 <= j < J_MAX
            and LINES[i][j] != "#"
        ):
            QUEUE.append(((i, j), step_count))


def take_steps():
    QUEUE.append(((SI, SJ), 0))
    while QUEUE:
        (si, sj), step_count = QUEUE.popleft()
        if (si, sj) in VISITED:
            continue
        VISITED[(si, sj)] = step_count
        take_step_from(si, sj, step_count)


def num_points_where(f):
    return sum(f(v) for v in VISITED.values())


def part_1():
    take_steps()
    return num_points_where(lambda v: v < STEPS_TO_EDGE and v % 2 == 0)


def part_2():
    n = (26501365 - STEPS_TO_EDGE) // GRID_SIZE
    assert n == 202300, f"n calc wrong, got {n}"
    num_odd_tiles = (n + 1) ** 2
    num_even_tiles = n**2
    odd_corners = num_points_where(lambda v: v > STEPS_TO_EDGE and v % 2 == 1)
    even_corners = num_points_where(lambda v: v > STEPS_TO_EDGE and v % 2 == 0)
    result = (
        num_odd_tiles * num_points_where(lambda v: v % 2 == 1)
        + num_even_tiles * num_points_where(lambda v: v % 2 == 0)
        - ((n + 1) * odd_corners)
        + (n * even_corners)
    )
    return result


p1_result = part_1()
p2_result = part_2()

p1_expected, p2_expected = expected_for_day(DAY)
assert p1_result == p1_expected
assert p2_result == p2_expected
print(f"{DAY} Part 1: {p1_result}")
print(f"{DAY} Part 2: {p2_result}")
