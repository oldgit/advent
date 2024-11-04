import sys

from util import expected_for_day

DAY = sys.argv[0].split(".")[0]


def transpose(matrix):
    """Swap the rows and columns of a 2-D matrix."""
    # transpose([(1, 2, 3), (11, 22, 33)]) --> (1, 11) (2, 22) (3, 33)
    return list(zip(*matrix, strict=True))


def find_mirror(matrix, with_smudge):
    for r in range(1, len(matrix)):
        above = matrix[:r][::-1]
        below = matrix[r:]

        above = above[: len(below)]
        below = below[: len(above)]

        if not with_smudge and above == below:
            return r

        if (
            with_smudge
            and sum(
                sum(0 if a == b else 1 for a, b in zip(x, y))
                for x, y in zip(above, below)
            )
            == 1
        ):
            return r

    return 0


with open(f"{DAY}/input.txt") as fin:
    patterns_in = fin.read().strip().split("\n\n")


def find_total(patterns, with_smudge):
    total = 0
    for pattern in patterns:
        matrix = pattern.splitlines()

        row = find_mirror(matrix, with_smudge)
        total += row * 100

        col = find_mirror(transpose(matrix), with_smudge)
        total += col

    return total


p1_result = find_total(patterns_in, False)
p2_result = find_total(patterns_in, True)

p1_expected, p2_expected = expected_for_day(DAY)
assert p1_result == p1_expected
assert p2_result == p2_expected
print(f"{DAY} Part 1: {p1_result}")
print(f"{DAY} Part 2: {p2_result}")
