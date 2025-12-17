import sys

from util import expected_for_day

DAY = sys.argv[0].split("/")[-1].split(".")[0]

with open(f"data/{DAY}/input.txt", "r") as file:
    DATA = file.read().strip()


def solve(part2=False):
    A = []
    space = []
    file_id = 0
    FINAL = []
    pos = 0
    for i, c in enumerate(DATA):
        if i % 2 == 0:
            if part2:
                A.append((pos, int(c), file_id))
            for i in range(int(c)):
                FINAL.append(file_id)
                if not part2:
                    A.append((pos, 1, file_id))
                pos += 1
            file_id += 1
        else:
            space.append((pos, int(c)))
            for i in range(int(c)):
                FINAL.append(None)
                pos += 1

    for pos, sz, file_id in reversed(A):
        for space_i, (space_pos, space_sz) in enumerate(space):
            if space_pos < pos and sz <= space_sz:
                for i in range(sz):
                    assert FINAL[pos + i] == file_id, f"{FINAL[pos+i]=}"
                    FINAL[pos + i] = None
                    FINAL[space_pos + i] = file_id
                space[space_i] = (space_pos + sz, space_sz - sz)
                break

    ans = 0
    for i, c in enumerate(FINAL):
        if c is not None:
            ans += i * c
    return ans


p1_result = solve()
p2_result = solve(True)

p1_expected, p2_expected = expected_for_day(DAY)
assert p1_result == p1_expected
assert p2_result == p2_expected
print(f"{DAY} Part 1: {p1_result}")
print(f"{DAY} Part 2: {p2_result}")
