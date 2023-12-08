lines = open(0).readlines()
path = lines[0].strip()
graph = {l[0:3]: (l[7:10], l[12:15]) for l in lines[2:]}
n, i = "AAA", 0

while n != "ZZZ":
    d = ["L", "R"].index(path[i % len(path)])
    n = graph[n][d]
    i += 1

print(i)
