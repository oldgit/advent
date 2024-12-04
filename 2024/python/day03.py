import re
import sys
from util import expected_for_day

DAY = sys.argv[0].split("/")[-1].split(".")[0]


with open(f"data/{DAY}/input.txt", "r") as file:
    DATA = "".join(file.readlines())


def sum_multiples(data, is_part2=False):
    result = 0
    do = True
    for m in re.finditer(r"mul\((\d{1,3}),(\d{1,3})\)|don't\(\)|do\(\)", data):
        if m.group(0) == "don't()":
            do = False if is_part2 else True
        elif m.group(0) == "do()":
            do = True
        else:
            if do:
                x, y = [int(s) for s in m.group(1, 2)]
                result += x * y
    return result


p1_result = sum_multiples(DATA)
p2_result = sum_multiples(DATA, True)

p1_expected, p2_expected = expected_for_day(DAY)
assert p1_result == p1_expected
assert p2_result == p2_expected
print(f"{DAY} Part 1: {p1_result}")
print(f"{DAY} Part 2: {p2_result}")
