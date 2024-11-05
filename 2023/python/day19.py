import sys

from util import expected_for_day

DAY = sys.argv[0].split("/")[-1].split(".")[0]

with open(f"data/{DAY}/input.txt") as fin:
    workflow_txt, part_txt = fin.read().split("\n\n")

OPS = {">": int.__gt__, "<": int.__lt__}


def get_workflows():
    workflows = {}
    for line in workflow_txt.splitlines():
        name, rest = line[:-1].split("{")
        rules = rest.split(",")
        workflows[name] = ([], rules.pop())
        for rule in rules:
            comparison, target = rule.split(":")
            key = comparison[0]
            cmp = comparison[1]
            n = int(comparison[2:])
            workflows[name][0].append((key, cmp, n, target))

    return workflows


def derive_part_ratings(part_line):
    part_ratings = {}
    for kv in part_line[1:-1].split(","):
        k, v = kv.split("=")
        part_ratings[k] = int(v)
    return part_ratings


def accept(workflows, part_ratings, name):
    if name == "R":
        return False
    if name == "A":
        return True

    rules, fallback = workflows[name]

    for key, cmp, n, target in rules:
        if OPS[cmp](part_ratings[key], n):
            return accept(workflows, part_ratings, target)

    return accept(workflows, part_ratings, fallback)


def valid_range(low_high: tuple):
    return low_high[0] <= low_high[1]


def count(category_ranges, workflows, workflow_name):
    # print(workflow_name)
    # print(category_ranges)
    if workflow_name == "R":
        return 0
    if workflow_name == "A":
        combinations = 1
        for lo, hi in category_ranges.values():
            combinations *= hi - lo + 1
        return combinations

    rules, fallback = workflows[workflow_name]
    total = 0

    valid_category_ranges = True
    for key, cmp, n, target in rules:
        lo, hi = category_ranges[key]
        if cmp == "<":
            t = (lo, n - 1)
            f = (n, hi)
        else:
            t = (n + 1, hi)
            f = (lo, n)
        if valid_range(t):
            copy = dict(category_ranges)
            copy[key] = t
            total += count(copy, workflows, target)
        if valid_range(f):
            category_ranges = dict(category_ranges)
            category_ranges[key] = f
        else:
            valid_category_ranges = False
            break
    if valid_category_ranges:
        total += count(category_ranges, workflows, fallback)

    return total


def part_1():
    total = 0
    workflows = get_workflows()
    for line in part_txt.splitlines():
        part_ratings = derive_part_ratings(line)
        if accept(workflows, part_ratings, "in"):
            total += sum(part_ratings.values())
    return total


def part_2():
    category_ranges = {key: (1, 4000) for key in "xmas"}
    workflows = get_workflows()
    return count(category_ranges, workflows, "in")


p1_result = part_1()
p2_result = part_2()

p1_expected, p2_expected = expected_for_day(DAY)
assert p1_result == p1_expected
assert p2_result == p2_expected
print(f"{DAY} Part 1: {p1_result}")
print(f"{DAY} Part 2: {p2_result}")
