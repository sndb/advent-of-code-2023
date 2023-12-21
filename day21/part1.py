from collections import deque

grid = open(0).read().splitlines()
queue = deque([(len(grid) // 2, len(grid[0]) // 2, 0)])
seen = set()
target = 64
answer = 0

while queue:
    r, c, s = queue.popleft()
    if s == target:
        answer += 1
    if s > target:
        break
    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nr, nc, ns = r + dr, c + dc, s + 1
        if grid[nr][nc] == "#":
            continue
        if (nr, nc, ns) in seen:
            continue
        seen.add((nr, nc, ns))
        queue.append((nr, nc, ns))

print(answer)
