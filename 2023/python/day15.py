import sys

from util import expected_for_day

DAY = sys.argv[0].split("/")[-1].split(".")[0]

with open(f"data/{DAY}/input.txt") as fin:
    steps_in = fin.read().strip().split(",")


def hash_string(text):
    result = 0
    for c in text:
        result = ((result + ord(c)) * 17) % 256
    return result


def part_1(steps):
    return sum(hash_string(s) for s in steps)


boxes = [[] for _ in range(256)]


def part_2(steps):
    for part in steps:
        if "-" in part:
            label = part[: part.index("-")]
            box = hash_string(label)
            lens = list(filter(lambda x: x[0] == label, boxes[box]))
            if len(lens) > 0:
                idx = boxes[box].index(lens[0])
                boxes[box].pop(idx)

        if "=" in part:
            label = part[: part.index("=")]
            box = hash_string(label)
            focal_len = int(part[part.index("=") + 1 :])
            lens = list(filter(lambda x: x[0] == label, boxes[box]))
            if len(lens) > 0:
                idx = boxes[box].index(lens[0])
                boxes[box][idx] = [label, focal_len]
            else:
                boxes[box].append([label, focal_len])

    ans = 0
    for i, box in enumerate(boxes):
        power = 0
        for j, lens in enumerate(box):
            power += (1 + i) * (j + 1) * lens[1]
        ans += power
    return ans


p1_result = part_1(steps_in)
p2_result = part_2(steps_in)

p1_expected, p2_expected = expected_for_day(DAY)
assert p1_result == p1_expected
assert p2_result == p2_expected
print(f"{DAY} Part 1: {p1_result}")
print(f"{DAY} Part 2: {p2_result}")
