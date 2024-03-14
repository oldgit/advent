with open("day09/input.txt") as fin:
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

print("Part 1:", sum(p1_ans))
print("Part 2:", sum(p2_ans))
