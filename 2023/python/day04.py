import sys
from collections import Counter

from util import expected_for_day

DAY = sys.argv[0].split("/")[-1].split(".")[0]

"""
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
"""

CARDS = []


def get_card_points(line):
    (win_text, num_text) = line.split(":")[1].split(" | ")
    wins = win_text.split()
    nums = num_text.split()
    CARDS.append((wins, nums))
    result = 0
    for win in wins:
        if win in nums:
            if result == 0:
                result = 1
            else:
                result = result * 2
    return result


pt1_result = 0
pt2_card_copies = Counter()
with open(f"data/{DAY}/input.txt", "r") as file:
    for line_in in file.read().splitlines():
        pt1_result = pt1_result + get_card_points(line_in)

for i, card in enumerate(CARDS):
    card_id = i + 1
    # Add the original card as a copy.
    pt2_card_copies[card_id] += 1

    wins2 = card[0]
    nums2 = card[1]
    matches = 0
    for n in nums2:
        if n in wins2:
            matches += 1

    max_card_id = len(CARDS)
    for copy_id in range(card_id + 1, card_id + matches + 1):
        if copy_id <= max_card_id:
            pt2_card_copies[copy_id] += pt2_card_copies[card_id]

pt2_result = sum(pt2_card_copies.values())

p1_expected, p2_expected = expected_for_day(DAY)
assert pt1_result == p1_expected
assert pt2_result == p2_expected
print(f"{DAY} Part 1: {pt1_result}")
print(f"{DAY} Part 2: {pt2_result}")
