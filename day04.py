from collections import Counter

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
    (wint, numt) = line.split(":")[1].split(" | ")
    wins = wint.split()
    nums = numt.split()
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
with open("day04/input.txt", "r") as file:
    for line in file.read().splitlines():
        pt1_result = pt1_result + get_card_points(line)

for i, card in enumerate(CARDS):
    card_id = i + 1
    # Add the original card as a copy.
    pt2_card_copies[card_id] += 1

    wins = card[0]
    nums = card[1]
    matches = 0
    for n in nums:
        if n in wins:
            matches += 1

    max_card_id = len(CARDS)
    for copy_id in range(card_id + 1, card_id + matches + 1):
        if copy_id <= max_card_id:
            pt2_card_copies[copy_id] += pt2_card_copies[card_id]

print("Part 1:", pt1_result)
print("Part 2:", sum(pt2_card_copies.values()))
