import sys
from util import expected_for_day

DAY = sys.argv[0].split("/")[-1].split(".")[0]

DIGITS = {str(i): i for i in range(1, 10)}

DIGIT_WORDS = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def calibration(line, digit_map):
    start = None
    end = None
    for i, _ in enumerate(line):
        for key, val in digit_map.items():
            if line[i:].startswith(key):
                if start is None:
                    start = val
                end = val
    assert start is not None
    assert end is not None
    return (start * 10) + end


with open(f"data/{DAY}/input.txt", "r") as file:
    LINES = file.read().splitlines()

p1_result = 0
p2_result = 0
for line_in in LINES:
    p1_result += calibration(line_in, DIGITS)
    p2_result += calibration(line_in, DIGITS | DIGIT_WORDS)

p1_expected, p2_expected = expected_for_day(DAY)
assert p1_result == p1_expected
assert p2_result == p2_expected
print(f"{DAY} Part 1: {p1_result}")
print(f"{DAY} Part 2: {p2_result}")
