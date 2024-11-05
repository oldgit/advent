import sys

from util import expected_for_day

DAY = sys.argv[0].split("/")[-1].split(".")[0]

with open(f"data/{DAY}/input.txt") as fin:
    LINES = fin.read().strip().split("\n")

n, m = len(LINES), len(LINES[0])

# Find starting point si, sj
si, sj = None, None
for GI, LINE in enumerate(LINES):
    if "S" in LINE:
        si, sj = GI, LINE.index("S")
        break
assert si is not None
assert sj is not None


dirs = {
    "|": [(1, 0), (-1, 0)],
    "-": [(0, 1), (0, -1)],
    "L": [(-1, 0), (0, 1)],
    "J": [(-1, 0), (0, -1)],
    "7": [(1, 0), (0, -1)],
    "F": [(1, 0), (0, 1)],
    ".": [],
}


def get_numbers(i, j):
    res = []
    for di, dj in list(dirs[LINES[i][j]]):
        ii, jj = i + di, j + dj
        if not (0 <= ii < n and 0 <= jj < m):
            continue
        res.append((ii, jj))
    return res


def find_start_pipe():
    didjs = []  # Values of di and dj that link up
    for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        ii, jj = si + di, sj + dj
        if not (0 <= ii < n and 0 <= jj < m):
            continue
        if (si, sj) in list(get_numbers(ii, jj)):
            didjs.append((di, dj))

    # Find which character corresponds to this one
    # "ds" for "dirs"
    for char, ds in dirs.items():
        if sorted(ds) == sorted(didjs):
            LINES[si] = LINES[si].replace("S", char)
            break


find_start_pipe()

visited = set()
stack = [(si, sj)]
while len(stack) > 0:
    top = stack.pop()
    if top in visited:
        continue
    visited.add(top)

    for nbr in list(get_numbers(*top)):
        if nbr in visited:
            continue
        stack.append(nbr)


# Count the number of "inversions" in a row
def count_inversions(i, j):
    # Everything up to (but not including) j in line i
    line = LINES[i]
    count = 0
    for k in range(j):
        if (i, k) not in visited:
            continue
        count += line[k] in {"J", "L", "|"}

    return count


p1_result = len(visited) // 2
p2_result = 0
for GI, LINE in enumerate(LINES):
    for J in range(m):
        if (GI, J) not in visited:
            invs = count_inversions(GI, J)
            if invs % 2 == 1:
                p2_result += 1


p1_expected, p2_expected = expected_for_day(DAY)
assert p1_result == p1_expected
assert p2_result == p2_expected
print(f"{DAY} Part 1: {p1_result}")
print(f"{DAY} Part 2: {p2_result}")
