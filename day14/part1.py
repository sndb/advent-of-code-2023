grid = list(map(list, open(0).read().splitlines()))
nr, nc = len(grid), len(grid[0])

def roll(g):
    for c in range(nc):
        j = 0
        for r in range(nr):
            if g[r][c] == "#":
                j = r
            if g[r][c] == "O":
                g[r][c] = "."
                while g[j][c] != ".":
                    j += 1
                g[j][c] = "O"
    return g

roll(grid)

total = 0

for c in range(nc):
    for r in range(nr):
        if grid[r][c] == "O":
            total += nr - r

print(total)
