import numpy as np
from collections import deque

grid = open(0).read().splitlines()
queue = deque([(len(grid) // 2, len(grid[0]) // 2, 0)])
seen = set()
xs = {65: 0, 196: 0, 327: 0}

while queue:
    r, c, s = queue.popleft()
    if s in xs:
        xs[s] += 1
    if s > max(xs.keys()):
        break
    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nr, nc, ns = r + dr, c + dc, s + 1
        if grid[nr % len(grid)][nc % len(grid[0])] == "#":
            continue
        if (nr, nc, ns) in seen:
            continue
        seen.add((nr, nc, ns))
        queue.append((nr, nc, ns))

p = np.polyfit(list(xs.keys()), list(xs.values()), 2)
print(round(np.polyval(p, 26501365)))
