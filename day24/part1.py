import numpy as np

low = 200000000000000
high = 400000000000000
positions = []
velocities = []

for line in open(0):
    pp, vv = line.split(" @ ")
    positions.append(list(map(int, pp.split(", "))))
    velocities.append(list(map(int, vv.split(", "))))

answer = 0

for i in range(len(positions)):
    for j in range(i + 1, len(positions)):
        xa, ya, _ = positions[i]
        xb, yb, _ = positions[j]
        dxa, dya, _ = velocities[i]
        dxb, dyb, _ = velocities[j]
        if dxa / dxb == dya / dyb:
            continue
        cs = [[dxa, -dxb], [dya, -dyb]]
        vs = [xa - xb, ya - yb]
        r = np.linalg.solve(cs, vs)
        if r[0] > 0 or r[1] > 0:
            continue
        rx = xa - dxa * r[0]
        ry = ya - dya * r[0]
        if low <= rx <= high and low <= ry <= high:
            answer += 1

print(answer)
