import sys
from collections import defaultdict
from functools import cmp_to_key

from util import expected_for_day

DAY = sys.argv[0].split(".")[0]

WITH_JOKERS = False
LABELS = "AKQJT98765432"
JOKER_LABELS = "AKQT98765432J"


def get_type_p1(hand):
    counts = defaultdict(int)
    for x in hand:
        counts[x] += 1

    amounts = sorted(counts.values())
    if amounts == [5]:
        return 7
    if amounts == [1, 4]:
        return 6
    if amounts == [2, 3]:
        return 5
    if amounts == [1, 1, 3]:
        return 4
    if amounts == [1, 2, 2]:
        return 3
    if amounts == [1, 1, 1, 2]:
        return 2
    return 1


def get_type_p2(hand):
    counts = defaultdict(int)
    jokers = 0
    for x in hand:
        if x == "J":
            jokers += 1
        else:
            counts[x] += 1

    amounts = sorted(counts.values())
    if jokers >= 5 or amounts[-1] + jokers >= 5:
        return 7
    if jokers >= 4 or amounts[-1] + jokers >= 4:
        return 6

    # Try a full house
    if amounts[-1] + jokers >= 3:
        rem_jokers = amounts[-1] + jokers - 3
        if len(amounts) >= 2 and amounts[-2] + rem_jokers >= 2 or rem_jokers >= 2:
            return 5
        return 4

    if amounts[-1] + jokers >= 2:
        rem_jokers = amounts[-1] + jokers - 2
        if len(amounts) >= 2 and amounts[-2] + rem_jokers >= 2 or rem_jokers >= 2:
            return 3
        return 2

    return 1


def compare(a, b):
    # a and b are two hands
    rankA = (get_type_p2(a) if WITH_JOKERS else get_type_p1(a), a)
    rankB = (get_type_p2(b) if WITH_JOKERS else get_type_p1(b), b)
    labels = JOKER_LABELS if WITH_JOKERS else LABELS
    if rankA[0] == rankB[0]:
        if a == b:
            return 0
        for i, j in zip(a, b):
            if labels.index(i) < labels.index(j):
                return 1
            if labels.index(i) > labels.index(j):
                return -1
        return -1
    if rankA[0] > rankB[0]:
        return 1
    return -1


LINES = []
with open(f"{DAY}/input.txt") as fin:
    raw_lines = fin.read().strip().split("\n")
    for line in raw_lines:
        hand_bid = line.split()
        LINES.append((hand_bid[0], int(hand_bid[1])))

pt1_result = 0
P1_LINES = sorted(LINES, key=cmp_to_key(lambda x, y: compare(x[0], y[0])))
for i, line in enumerate(P1_LINES):
    pt1_result += (i + 1) * line[1]

pt2_result = 0
WITH_JOKERS = True
P2_LINES = sorted(LINES, key=cmp_to_key(lambda x, y: compare(x[0], y[0])))
for i, line in enumerate(P2_LINES):
    pt2_result += (i + 1) * line[1]


p1_expected, p2_expected = expected_for_day(DAY)
assert pt1_result == p1_expected
assert pt2_result == p2_expected
print(f"{DAY} Part 1: {pt1_result}")
print(f"{DAY} Part 2: {pt2_result}")
