def extend(grid):
    res = []
    for row in grid:
        res.append(row)
        if set(row) == {"."}:
            res.append(row)
    return res


def distance(p, q):
    return abs(p[0] - q[0]) + abs(p[1] - q[1])


grid = [l.strip() for l in open(0)]
grid = extend(grid)
grid = extend(zip(*grid))

galaxies = []

for r in range(len(grid)):
    for c in range(len(grid[0])):
        if grid[r][c] == "#":
            galaxies.append((r, c))

total = 0

for i in range(len(galaxies)):
    for j in range(i + 1, len(galaxies)):
        total += distance(galaxies[i], galaxies[j])

print(total)
