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

def rotate(g):
    return list(map(list, map(reversed, zip(*g))))

def cycle(g):
    for _ in range(4):
        g = rotate(roll(g))
    return g

i, n, h = 0, 1000000000, {}

while i < n:
    k = tuple(map(str, grid))
    if j := h.get(k):
        c = i - j
        i += (n - i) // c * c
    h[k] = i
    grid = cycle(grid)
    i += 1

total = 0

for c in range(nc):
    for r in range(nr):
        if grid[r][c] == "O":
            total += nr - r

print(total)
