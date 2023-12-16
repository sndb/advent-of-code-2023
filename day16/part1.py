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

queue = [((0, 0), (0, 1))]
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

print(len(beams))
