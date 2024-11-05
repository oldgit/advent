import math
import re
import sys

from util import expected_for_day

DAY = sys.argv[0].split("/")[-1].split(".")[0]

NODES = {}

with open(f"data/{DAY}/input.txt") as fin:
    raw_lines = fin.read().strip().split("\n")
    STEPS = raw_lines[0]
    for line in raw_lines[2:]:
        search = re.search(r"(...) = \((...), (...)\)", line)
        assert search is not None
        parent, left, right = search.groups(0)
        NODES[parent] = (left, right)

CUR = "AAA"
COUNT = 0
while CUR != "ZZZ":
    STEP = STEPS[COUNT % len(STEPS)]
    if STEP == "L":
        CUR = NODES[CUR][0]
    else:
        CUR = NODES[CUR][1]
    COUNT += 1


def n_steps(cur):
    count = 0
    while cur[2] != "Z":
        step = STEPS[count % len(STEPS)]
        if step == "L":
            cur = NODES[cur][0]
        else:
            cur = NODES[cur][1]
        count += 1
    return count


start_nodes = [n for n in NODES if n[2] == "A"]
steps = [n_steps(node) for node in start_nodes]

p1_result = COUNT
p2_result = math.lcm(*steps)

p1_expected, p2_expected = expected_for_day(DAY)
assert p1_result == p1_expected
assert p2_result == p2_expected
print(f"{DAY} Part 1: {p1_result}")
print(f"{DAY} Part 2: {p2_result}")
