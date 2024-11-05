from collections import defaultdict
import sys

from util import expected_for_day

sys.setrecursionlimit(1000000)

DAY = sys.argv[0].split("/")[-1].split(".")[0]

SLOPE_DIRS = {"^": (-1, 0), "v": (1, 0), ">": (0, 1), "<": (0, -1)}
SLOPES = list(SLOPE_DIRS.keys())
DIRS = list(SLOPE_DIRS.values())
BEST = 0


with open(f"data/{DAY}/input.txt") as fin:
    GRID = [list(line) for line in fin.read().strip().split("\n")]
    N, M = len(GRID), len(GRID[0])

START_POINT = (0, 1)
END_POINT = (N - 1, M - 2)


def adjacent(current: tuple[int, int], pt1: bool):
    cx, cy = current
    adjacent_s = DIRS
    if pt1 and GRID[cx][cy] in SLOPES:
        adjacent_s = [(SLOPE_DIRS[GRID[cx][cy]])]
    for dx, dy in adjacent_s:
        nx, ny = cx + dx, cy + dy
        if nx in range(N) and ny in range(M) and GRID[nx][ny] != "#":
            yield nx, ny


def get_junction_vertices(pt1: bool):
    vs = set()
    for i in range(N):
        for j in range(M):
            if GRID[i][j] != "#":
                num_adjacent = len(list(adjacent((i, j), pt1)))
                if num_adjacent > 2:
                    vs.add((i, j))
    vs.add(START_POINT)
    vs.add(END_POINT)
    return vs


def build_compressed_graph(junction_vertices: set[tuple[int, int]], pt1: bool):
    graph_dict = defaultdict(list)
    for x, y in junction_vertices:
        q = [(x, y)]
        seen = {(x, y)}
        dist = 0
        while len(q) > 0:
            nq = []
            dist += 1
            for c in q:
                for a in adjacent(c, pt1):
                    if a not in seen:
                        seen.add(a)
                        if a in junction_vertices:
                            graph_dict[x, y].append((dist, a))
                        else:
                            nq.append(a)
            q = nq
    return graph_dict


def dfs(
    graph_dict: defaultdict[tuple[int, int], list[tuple[int, tuple[int, int]]]],
    current: tuple[int, int],
    path_set: set[tuple[int, int]],
    total_dist: int,
):
    global BEST
    if current == (N - 1, M - 2) and total_dist > BEST:
        BEST = max(BEST, total_dist)
    for dist, a in graph_dict[current]:
        if a not in path_set:
            path_set.add(a)
            dfs(graph_dict, a, path_set, total_dist + dist)
            path_set.remove(a)


def part_1():
    pt1 = True
    v = get_junction_vertices(pt1)
    g = build_compressed_graph(v, pt1)
    dfs(g, (0, 1), set(), 0)
    return BEST


def part_2():
    global BEST
    BEST = 0
    pt1 = False
    v = get_junction_vertices(pt1)
    g = build_compressed_graph(v, pt1)
    dfs(g, (0, 1), set(), 0)
    return BEST


p1_result = part_1()
p2_result = part_2()

p1_expected, p2_expected = expected_for_day(DAY)
assert p1_result == p1_expected
assert p2_result == p2_expected
print(f"{DAY} Part 1: {p1_result}")
print(f"{DAY} Part 2: {p2_result}")
