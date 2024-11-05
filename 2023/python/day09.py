import sys

from util import expected_for_day

DAY = sys.argv[0].split("/")[-1].split(".")[0]

with open(f"data/{DAY}/input.txt") as fin:
    lines = fin.read().strip().split("\n")


def diff(arr):
    return [arr[i + 1] - arr[i] for i in range(len(arr) - 1)]


def extrapolate(hist):
    layers = [hist]
    while not all([x == 0 for x in layers[-1]]):
        layers.append(diff(layers[-1]))

    layers[-1].append(0)
    for i in range(len(layers) - 2, -1, -1):
        layers[i].append(layers[i][-1] + layers[i + 1][-1])

    return layers[0][-1]


p1_ans = []
p2_ans = []
for line in lines:
    arr1 = list(map(int, line.split()))
    p1_ans.append(extrapolate(arr1))
    arr2 = list(map(int, line.split()[::-1]))
    p2_ans.append(extrapolate(arr2))

p1_result = sum(p1_ans)
p2_result = sum(p2_ans)


p1_expected, p2_expected = expected_for_day(DAY)
assert p1_result == p1_expected
assert p2_result == p2_expected
print(f"{DAY} Part 1: {p1_result}")
print(f"{DAY} Part 2: {p2_result}")
