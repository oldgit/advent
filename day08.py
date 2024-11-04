import sys
import math
import re

from util import expected_for_day

DAY = sys.argv[0].split(".")[0]

STEPS = ""
NODES = {}

with open(f"{DAY}/input.txt") as fin:
    raw_lines = fin.read().strip().split("\n")
    STEPS = raw_lines[0]
    for line in raw_lines[2:]:
        search = re.search(r"(...) = \((...), (...)\)", line)
        assert search is not None
        parent, left, right = search.groups(0)
        NODES[parent] = (left, right)

cur = "AAA"
count = 0
while cur != "ZZZ":
    step = STEPS[count % len(STEPS)]
    if step == "L":
        cur = NODES[cur][0]
    else:
        cur = NODES[cur][1]
    count += 1


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

p1_result = count
p2_result = math.lcm(*steps)


p1_expected, p2_expected = expected_for_day(DAY)
assert p1_result == p1_expected
assert p2_result == p2_expected
print(f"{DAY} Part 1: {p1_result}")
print(f"{DAY} Part 2: {p2_result}")
