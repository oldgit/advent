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


def calibration(line, digitMap):
    start = None
    end = None
    for i, _ in enumerate(line):
        for key, val in digitMap.items():
            if line[i:].startswith(key):
                if start is None:
                    start = val
                end = val
    return (start * 10) + end


LINES = []
with open("day01/input.txt", "r") as file:
    LINES = file.read().splitlines()

p1_result = 0
p2_result = 0
for line in LINES:
    p1_result += calibration(line, DIGITS)
    p2_result += calibration(line, DIGITS | DIGIT_WORDS)

print("Part 1:", p1_result)
print("Part 2:", p2_result)
