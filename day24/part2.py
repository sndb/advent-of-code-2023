from sympy import symbols, solve

positions = []
velocities = []

for line in open(0):
    pp, vv = line.split(" @ ")
    positions.append(list(map(int, pp.split(", "))))
    velocities.append(list(map(int, vv.split(", "))))

xr, yr, zr, dxr, dyr, dzr = symbols("xr yr zr dxr dyr dzr")

equations = []

for i in range(len(positions)):
    xh, yh, zh = positions[i]
    dxh, dyh, dzh = velocities[i]
    e1 = (xr - xh) * (dyh - dyr) - (yr - yh) * (dxh - dxr)
    e2 = (xr - xh) * (dzh - dzr) - (zr - zh) * (dxh - dxr)
    equations.extend([e1, e2])

s = solve(equations)[0]
print(s[xr] + s[yr] + s[zr])
