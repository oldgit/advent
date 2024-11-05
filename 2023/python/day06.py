import sys

from util import expected_for_day

DAY = sys.argv[0].split("/")[-1].split(".")[0]


with open(f"data/{DAY}/input.txt", "r") as file:
    T, D = file.read().splitlines()
    TIMES = [int(x) for x in T.split(":")[1].split()]
    DIST = [int(x) for x in D.split(":")[1].split()]


def f_simple(t, d):
    ans = 0
    for x in range(t):
        dx = x * (t - x)
        if dx > d:
            ans += 1
    return ans


def f_binary(t, d):
    # runs in O(log(t))
    # let g(x) = x*(t-x) is maximized at t//2
    # we want to know: what is the lowest value s.t. g(x) >= d
    # we want to know: what is the highest value s.t. g(x) >= d
    def g(x):
        return x * (t - x)

    lo = 0
    hi = t // 2
    if hi * (t - hi) < d:
        return 0
    assert g(lo) < d <= g(hi)
    while lo + 1 < hi:
        m = (lo + hi) // 2
        if g(m) >= d:
            hi = m
        else:
            lo = m
    assert lo + 1 == hi
    assert g(lo) < d <= g(hi)
    first = hi
    assert g(first) >= d > g(first - 1)

    # g(x) == g(t-x), so there's symmetry about the midpoint t/2
    last = int((t / 2) + (t / 2 - first))
    assert (
        g(last) >= d > g(last + 1)
    ), f"last={last} g(last)={g(last)} {g(last + 1)} d={d}"
    return last - first + 1


pt1_ans = 1
for i in range(len(TIMES)):
    pt1_ans *= f_simple(TIMES[i], DIST[i])

pt2_time = int("".join(map(str, TIMES)))
pt2_dist = int("".join(map(str, DIST)))
pt2_ans = f_binary(pt2_time, pt2_dist)

p1_expected, p2_expected = expected_for_day(DAY)
assert pt1_ans == p1_expected
assert pt2_ans == p2_expected
print(f"{DAY} Part 1: {pt1_ans}")
print(f"{DAY} Part 2: {pt2_ans}")
