import itertools
import sys

from util import expected_for_day

DAY = sys.argv[0].split("/")[-1].split(".")[0]

MUL = 0
ADD = 1
CAT = 2


with open(f"data/{DAY}/input.txt", "r") as file:
    DATA = []
    for r in file.read().strip().split("\n"):
        a, e = r.split(":")
        DATA.append((int(a), list(map(lambda x: int(x), e.split()))))


def solve(data, part_2=False):
    result = 0
    false_eqs = []
    operators = (MUL, ADD, CAT) if part_2 else (MUL, ADD)
    for expected, nums in data:
        n_result = 0
        for ops in itertools.product(*[operators for _ in range(len(nums) - 1)]):
            ans = nums[0]
            for i in range(1, len(nums)):
                op = ops[i - 1]
                if op == CAT:
                    ans = int(str(ans) + str(nums[i]))
                elif op == MUL:
                    ans *= nums[i]
                elif op == ADD:
                    ans += nums[i]
            if ans == expected:
                n_result = expected
                break
        result += n_result
        if n_result == 0:
            false_eqs.append((expected, nums))
    return result, false_eqs


p1_result, falsies = solve(DATA)
p2_result = p1_result + solve(falsies, True)[0]

p1_expected, p2_expected = expected_for_day(DAY)
assert p1_result == p1_expected
assert p2_result == p2_expected
print(f"{DAY} Part 1: {p1_result}")
print(f"{DAY} Part 2: {p2_result}")
