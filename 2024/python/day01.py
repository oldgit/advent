import sys
from util import expected_for_day

DAY = sys.argv[0].split("/")[-1].split(".")[0]


with open(f"data/{DAY}/input.txt", "r") as file:
    LIST_1 = []
    LIST_2 = []
    while line := file.readline():
        l1, l2 = line.split()
        LIST_1.append(int(l1))
        LIST_2.append(int(l2))


def part1(list_1, list_2):
    slist_1 = sorted(list_1)
    slist_2 = sorted(list_2)
    result = 0
    for i, val_1 in enumerate(slist_1):
        result += abs(val_1 - slist_2[i])
    return result


def part2(list_1, list_2):
    result = 0
    for value in list_1:
        hits = [x for x in list_2 if x == value]
        result += value * len(hits)
    return result


p1_result = part1(LIST_1, LIST_2)
p2_result = part2(LIST_1, LIST_2)

p1_expected, p2_expected = expected_for_day(DAY)
assert p1_result == p1_expected
# assert p2_result == p2_expected
print(f"{DAY} Part 1: {p1_result}")
print(f"{DAY} Part 2: {p2_result}")
