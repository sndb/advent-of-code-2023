grid = open(0).read().splitlines()
dest = (140, 139)
queue = [(0, 0, 1, tuple())]
answer = 0

while queue:
    d, r, c, path = queue.pop()

    if (r, c) == dest:
        answer = max(answer, d)
        continue

    if (r, c) in path:
        continue
    path += ((r, c),)

    if grid[r][c] == ">":
        queue.append((d + 1, r, c + 1, path))
    elif grid[r][c] == "v":
        queue.append((d + 1, r + 1, c, path))
    else:
        for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
            if (
                nr >= 0
                and nr < len(grid)
                and nc >= 0
                and nc < len(grid[0])
                and grid[nr][nc] != "#"
            ):
                queue.append((d + 1, nr, nc, path))

print(answer)
