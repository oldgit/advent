import sys
from collections import defaultdict

from util import expected_for_day

DAY = sys.argv[0].split(".")[0]

BRICKS = []

with open(f"{DAY}/input.txt") as fin:
    LINES = fin.read().strip().split("\n")
    for LINE in LINES:
        a, b = LINE.split("~")
        a = list(map(int, a.split(",")))
        b = list(map(int, b.split(",")))
        BRICKS.append((a, b))

BRICKS_TOTAL = len(BRICKS)
BRICKS.sort(key=lambda x: x[0][2])

HIGHEST = defaultdict(lambda: (0, -1))
BAD = set()
GRAPH = [[] for i in range(BRICKS_TOTAL)]
for index, brick in enumerate(BRICKS):
    MAX_HEIGHT = -1
    SUPPORT_SET = set()
    for X in range(brick[0][0], brick[1][0] + 1):
        for Y in range(brick[0][1], brick[1][1] + 1):
            if HIGHEST[X, Y][0] + 1 > MAX_HEIGHT:
                MAX_HEIGHT = HIGHEST[X, Y][0] + 1
                SUPPORT_SET = {HIGHEST[X, Y][1]}
            elif HIGHEST[X, Y][0] + 1 == MAX_HEIGHT:
                SUPPORT_SET.add(HIGHEST[X, Y][1])

    for X in SUPPORT_SET:
        if X != -1:
            GRAPH[X].append(index)

    if len(SUPPORT_SET) == 1:
        bad = SUPPORT_SET.pop()
        if bad != -1:
            BAD.add(bad)

    fall = brick[0][2] - MAX_HEIGHT
    if fall > 0:
        brick[0][2] -= fall
        brick[1][2] -= fall

    for X in range(brick[0][0], brick[1][0] + 1):
        for Y in range(brick[0][1], brick[1][1] + 1):
            HIGHEST[X, Y] = (brick[1][2], index)


def count_other_bricks(idx, graph):
    index_grid = [0 for __ in range(BRICKS_TOTAL)]
    for j in range(BRICKS_TOTAL):
        for i in graph[j]:
            index_grid[i] += 1
    q = [idx]
    count = -1
    while len(q) > 0:
        count += 1
        x = q.pop()
        for i in graph[x]:
            index_grid[i] -= 1
            if index_grid[i] == 0:
                q.append(i)

    return count


def part_1():
    safe_bricks = len(BRICKS) - len(BAD)
    return safe_bricks


def part_2():
    other_bricks = [count_other_bricks(x, GRAPH) for x in range(BRICKS_TOTAL)]
    return sum(other_bricks)


p1_result = part_1()
p2_result = part_2()

p1_expected, p2_expected = expected_for_day(DAY)
assert p1_result == p1_expected
assert p2_result == p2_expected
print(f"{DAY} Part 1: {p1_result}")
print(f"{DAY} Part 2: {p2_result}")
