import sys

from util import expected_for_day

DAY = sys.argv[0].split(".")[0]

MIN = 200000000000000
MAX = 400000000000000
STONES = []

with open(f"{DAY}/input.txt") as fin:
    LINES = fin.read().strip().split("\n")
    for LINE in LINES:
        pos, vel = LINE.split(" @ ")
        pos = tuple(map(int, pos.split(",")))
        vel = tuple(map(int, vel.split(",")))
        STONES.append((pos, vel))


def subtract(a, b):
    ax, ay, az = a
    bx, by, bz = b
    return (ax - bx, ay - by, az - bz)


def dot_prod(a, b):
    ax, ay, az = a
    bx, by, bz = b
    return (ax * bx) + (ay * by) + (az * bz)


def cross_prod(a, b):
    c = [
        a[1] * b[2] - a[2] * b[1],
        a[2] * b[0] - a[0] * b[2],
        a[0] * b[1] - a[1] * b[0],
    ]
    return c


def new_pos(stone, time):
    pos, vel = stone
    x, y, z = pos
    dx, dy, dz = vel[0] * time, vel[1] * time, vel[2] * time
    return (x + dx, y + dy, z + dz)


def part_1():
    result = 0
    for i in range(len(STONES)):
        for j in range(i + 1, len(STONES)):
            ip, iv = STONES[i]
            jp, jv = STONES[j]
            dx = jp[0] - ip[0]
            dy = jp[1] - ip[1]
            det = (jv[0] * iv[1]) - (jv[1] * iv[0])
            if det == 0:
                continue
            u = (dy * jv[0] - dx * jv[1]) / det
            v = (dy * iv[0] - dx * iv[1]) / det
            if u < 0 or v < 0:
                continue
            xi = jp[0] + jv[0] * v
            yi = jp[1] + jv[1] * v
            if xi >= MIN and xi <= MAX and yi >= MIN and yi <= MAX:
                result += 1
    return result


def part_2():
    p0, v0 = STONES[0]
    p1 = subtract(STONES[1][0], p0)
    v1 = subtract(STONES[1][1], v0)
    p2 = subtract(STONES[2][0], p0)
    v2 = subtract(STONES[2][1], v0)

    t1 = -(dot_prod(cross_prod(p1, p2), v2)) / dot_prod(cross_prod(v1, p2), v2)
    t2 = -(dot_prod(cross_prod(p1, p2), v1)) / dot_prod(cross_prod(p1, v2), v1)

    c1 = new_pos(STONES[1], t1)
    c2 = new_pos(STONES[2], t2)
    dt = t2 - t1
    vx, vy, vz = ((c2[0] - c1[0]) / dt, (c2[1] - c1[1]) / dt, (c2[2] - c1[2]) / dt)
    rx = c1[0] - (vx * t1)
    ry = c1[1] - (vy * t1)
    rz = c1[2] - (vz * t1)

    return int(rx + ry + rz)


p1_result = part_1()
p2_result = part_2()

p1_expected, p2_expected = expected_for_day(DAY)
assert p1_result == p1_expected
assert p2_result == p2_expected
print(f"{DAY} Part 1: {p1_result}")
print(f"{DAY} Part 2: {p2_result}")
