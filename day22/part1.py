bricks = []

for l in open(0):
    bricks.append([list(map(int, x.split(","))) for x in l.split("~")])


def intersect(b1, b2):
    s1 = set(
        [
            (x, y)
            for x in range(b1[0][0], b1[1][0] + 1)
            for y in range(b1[0][1], b1[1][1] + 1)
        ]
    )
    s2 = set(
        [
            (x, y)
            for x in range(b2[0][0], b2[1][0] + 1)
            for y in range(b2[0][1], b2[1][1] + 1)
        ]
    )
    return s1 & s2


def distance(b1, b2):
    if not intersect(b1, b2):
        return None
    return min(b2[0][2], b2[1][2]) - max(b1[0][2], b1[1][2])


stacked = []

for b in sorted(bricks, key=lambda b: min(b[0][2], b[1][2])):
    sd = min(b[0][2], b[1][2])
    for s in stacked:
        d = distance(s, b)
        if d is not None and d < sd:
            sd = d
    b[0][2] -= sd - 1
    b[1][2] -= sd - 1
    stacked.append(b)

comp = [set() for _ in range(len(stacked))]
base = [set() for _ in range(len(stacked))]

for i in range(len(stacked)):
    for j in range(i):
        if distance(stacked[j], stacked[i]) == 1:
            comp[i].add(j)
            base[j].add(i)


answer = 0

for b in range(len(base)):
    for c in base[b]:
        if len(comp[c]) == 1:
            break
    else:
        answer += 1

print(answer)
