from math import lcm

lines = open(0).readlines()
path = lines[0].strip()
graph = {l[0:3]: (l[7:10], l[12:15]) for l in lines[2:]}
nodes = [p for p in graph.keys() if p[2] == "A"]
divs = []

for n in nodes:
    z, i = [], 0
    while len(z) < 2:
        d = ["L", "R"].index(path[i % len(path)])
        n = graph[n][d]
        if n[2] == "Z":
            z += [i]
        i += 1
    divs += [z[1] - z[0]]

print(lcm(*divs))
