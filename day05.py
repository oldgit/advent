BATCH_SIZE = 500000
SEEDS = []
MAPS = []
SEED_RANGES = []


def destination(source, amap):
    for k in amap:
        if source >= k[0] and source <= k[1]:
            return source + amap[k]


def get_min(start_min, s, e):
    # print("get_min:", start_min, s, e)
    for src in range(s, e):
        res = src
        for m in MAPS:
            res = destination(res, m)
        if res < start_min:
            start_min = res
    return start_min


with open("day05/input.txt", "r") as file:
    in_map = False
    amap = {}
    lines = file.read().splitlines()
    lines.append("")
    for line in lines:
        if line.startswith("seeds:"):
            SEEDS = [int(x) for x in line.split(":")[1].split()]
            for i in range(0, len(SEEDS), 2):
                SEED_RANGES.append((SEEDS[i], SEEDS[i + 1]))
        else:
            if line.endswith("map:"):
                in_map = True
            if in_map and line and line[0].isdigit():
                (dest, src, num) = map(lambda x: int(x), line.split())
                diff = dest - src
                amap[src] = (num, diff)
            if in_map and len(line) == 0:
                rmap = {}
                start = 0
                for k in sorted(amap):
                    if k > start:
                        rmap[(start, k - 1)] = 0
                    end_k = k + amap[k][0] - 1
                    rmap[(k, end_k)] = amap[k][1]
                    start = end_k + 1
                rmap[(start, 9999999999999)] = 0
                MAPS.append(rmap)
                amap = {}


p1_min = 999999999999
for seed in SEEDS:
    result = seed
    for m in MAPS:
        result = destination(result, m)
    if result < p1_min:
        p1_min = result

p2_min = 9999999999999
for start, num in SEED_RANGES:
    if num > BATCH_SIZE:
        batches = int(num / BATCH_SIZE)
        for batch in range(0, batches):
            print("batch: ", batch, batches, p2_min)
            result = get_min(
                p2_min,
                start + (batch * BATCH_SIZE),
                start - 1 + ((batch + 1) * BATCH_SIZE),
            )
            if result < p2_min:
                p2_min = result
        result = get_min(p2_min, batches * BATCH_SIZE + start, start + num - 1)
        if result < p2_min:
            p2_min = result

print("Part 1:", p1_min)
print("Part 2:", p2_min)
