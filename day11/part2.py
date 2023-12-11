def distance(p, q):
    d = 0
    for r in range(min(p[0], q[0]), max(p[0], q[0])):
        d += 1000000 if r in empty_rows else 1
    for c in range(min(p[1], q[1]), max(p[1], q[1])):
        d += 1000000 if c in empty_cols else 1
    return d


grid = [l.strip() for l in open(0)]
empty_rows = [r for r, row in enumerate(grid) if set(row) == {"."}]
empty_cols = [c for c, col in enumerate(zip(*grid)) if set(col) == {"."}]

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
