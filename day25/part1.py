from networkx import Graph, minimum_edge_cut

graph = {}

for line in open(0):
    a, bs = line.split(": ")
    for b in bs.split():
        graph.setdefault(a, []).append(b)
        graph.setdefault(b, []).append(a)

cut = minimum_edge_cut(Graph(graph))
queue = [list(graph.keys())[0]]
seen = set()

while queue:
    v = queue.pop()
    if v in seen:
        continue
    seen.add(v)
    for u in graph[v]:
        if (u, v) not in cut and (v, u) not in cut:
            queue.append(u)

print((len(graph) - len(seen)) * len(seen))
