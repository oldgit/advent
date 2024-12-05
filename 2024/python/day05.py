import sys
from functools import cmp_to_key
from util import expected_for_day

DAY = sys.argv[0].split("/")[-1].split(".")[0]


with open(f"data/{DAY}/input.txt", "r") as file:
    RULES = []
    UPDATES = []
    at_rules = True
    for LINE in file.readlines():
        at_rules = at_rules and LINE != "\n"
        if at_rules:
            a, b = map(lambda x: int(x), LINE.split("|"))
            RULES.append((a, b))
        elif LINE != "\n":
            UPDATES.append(list(map(lambda x: int(x), LINE.split(","))))


def compare_pages(x, y):
    # Swap pages which break rules
    if (x, y) in RULES:
        return -1
    elif (y, x) in RULES:
        return 1
    else:
        return 0


def solve(part2=False):
    total = 0
    for u in UPDATES:
        correct = True
        for i, p in enumerate(u):
            if i > 0:
                previous = u[:i]
                rules = [y for (x, y) in RULES if x == p]
                for rule_page in rules:
                    if any(x == rule_page for x in previous):
                        correct = False
                        break
            if not correct:
                break
        if part2:
            if not correct:
                reordered = sorted(u, key=cmp_to_key(compare_pages))
                middle = reordered[len(reordered) // 2]
                total += middle
        else:
            if correct:
                middle = u[len(u) // 2]
                total += middle
    return total


p1_result = solve()
p2_result = solve(True)

p1_expected, p2_expected = expected_for_day(DAY)
assert p1_result == p1_expected
assert p2_result == p2_expected
print(f"{DAY} Part 1: {p1_result}")
print(f"{DAY} Part 2: {p2_result}")
