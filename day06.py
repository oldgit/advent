LINES = []
with open("day06/input.txt", "r") as file:
    LINES = file.read().splitlines()

t, d = LINES
times = [int(x) for x in t.split(":")[1].split()]
dist = [int(x) for x in d.split(":")[1].split()]


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
    assert g(lo) < d and g(hi) >= d
    while lo + 1 < hi:
        m = (lo + hi) // 2
        if g(m) >= d:
            hi = m
        else:
            lo = m
    assert lo + 1 == hi
    assert g(lo) < d and g(hi) >= d
    first = hi
    assert g(first) >= d and g(first - 1) < d

    # g(x) == g(t-x), so there's symmetry about the midpoint t/2
    last = int((t / 2) + (t / 2 - first))
    assert (
        g(last) >= d and g(last + 1) < d
    ), f"last={last} g(last)={g(last)} {g(last+1)} d={d}"
    return last - first + 1


pt1_ans = 1
for i in range(len(times)):
    pt1_ans *= f_simple(times[i], dist[i])

pt2_time = int("".join(map(str, times)))
pt2_dist = int("".join(map(str, dist)))
pt2_ans = f_binary(pt2_time, pt2_dist)

print("Part 1:", pt1_ans)
print("Part 2:", pt2_ans)
