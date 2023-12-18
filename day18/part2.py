dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
area = r = c = 0

for l in open(0):
    x = int(l.split()[2][2:-1], 16)
    n, d = divmod(x, 16)
    dr, dc = dirs[d]
    nr, nc = r + dr * n, c + dc * n
    area += nr * c - nc * r + n
    r, c = nr, nc

print(area // 2 + 1)
