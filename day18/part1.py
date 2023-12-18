dirs = {"R": (0, 1), "U": (-1, 0), "L": (0, -1), "D": (1, 0)}
area = r = c = 0

for l in open(0):
    d, n, _ = l.split()
    n = int(n)
    dr, dc = dirs[d]
    nr, nc = r + dr * n, c + dc * n
    area += nr * c - nc * r + n
    r, c = nr, nc

print(area // 2 + 1)
