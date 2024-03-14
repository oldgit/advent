with open("day10/input.txt") as fin:
    lines = fin.read().strip().split("\n")

n, m = len(lines), len(lines[0])

# Find starting point si, sj
si, sj = None, None
for i, line in enumerate(lines):
    if "S" in line:
        si, sj = i, line.index("S")
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


def get_nbrs(i, j):
    res = []
    for di, dj in list(dirs[lines[i][j]]):
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
        if (si, sj) in list(get_nbrs(ii, jj)):
            didjs.append((di, dj))

    # Find which character corresponds to this one
    # "ds" for "dirs"
    for char, ds in dirs.items():
        if sorted(ds) == sorted(didjs):
            lines[si] = lines[si].replace("S", char)
            break


find_start_pipe()

visited = set()
stack = [(si, sj)]
while len(stack) > 0:
    top = stack.pop()
    if top in visited:
        continue
    visited.add(top)

    for nbr in list(get_nbrs(*top)):
        if nbr in visited:
            continue
        stack.append(nbr)


# Count the number of "inversions" in a row
def count_invs(i, j):
    # Everything up to (but not including) j in line i
    line = lines[i]
    count = 0
    for k in range(j):
        if (i, k) not in visited:
            continue
        count += line[k] in {"J", "L", "|"}

    return count


ans_pt2 = 0
for i, line in enumerate(lines):
    for j in range(m):
        if (i, j) not in visited:
            invs = count_invs(i, j)
            if invs % 2 == 1:
                ans_pt2 += 1

print("Part 1:", len(visited) // 2)
print("Part 2:", ans_pt2)
