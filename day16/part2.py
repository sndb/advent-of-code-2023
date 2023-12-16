from collections import defaultdict

grid = open(0).read().splitlines()
n = len(grid)

def reflect(t, d):
    r, c = d
    match t:
        case ".":
            yield d
        case "/":
            yield (-c, -r)
        case "\\":
            yield (c, r)
        case "|":
            if c != 0:
                yield (1, 0)
                yield (-1, 0)
            else:
                yield d
        case "-":
            if r != 0:
                yield (0, 1)
                yield (0, -1)
            else:
                yield d

def energize(source):
    queue = [source]
    beams = defaultdict(list)
    while queue:
        p, d = queue.pop()
        if d in beams[p]:
            continue
        beams[p].append(d)
        for r in reflect(grid[p[0]][p[1]], d):
            q = (p[0] + r[0], p[1] + r[1])
            if q[0] >= 0 and q[0] < n and q[1] >= 0 and q[1] < n:
                queue.append((q, r))
    return len(beams)

e = []

for i in range(n):
    e.append(((i, 0), (0, 1)))
    e.append(((i, n - 1), (0, -1)))
    e.append(((0, i), (1, 0)))
    e.append(((n - 1, i), (-1, 0)))

print(max(map(energize, e)))
