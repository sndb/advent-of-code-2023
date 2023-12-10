from math import inf

grid = [l.strip() for l in open(0)]


def adj(r, c):
    t = grid[r][c]
    if t == "S":
        t = "-"
    match t:
        case "|":
            return [(r - 1, c), (r + 1, c)]
        case "-":
            return [(r, c - 1), (r, c + 1)]
        case "L":
            return [(r - 1, c), (r, c + 1)]
        case "J":
            return [(r - 1, c), (r, c - 1)]
        case "7":
            return [(r + 1, c), (r, c - 1)]
        case "F":
            return [(r + 1, c), (r, c + 1)]
    return []


def walk(r, c):
    costs = {}
    queue = [(r, c, 0)]
    while len(queue) > 0:
        (r, c, cost) = queue.pop()
        if cost < costs.get((r, c), inf):
            costs[(r, c)] = cost
            for ar, ac in adj(r, c):
                queue.append((ar, ac, cost + 1))
    return costs


for r, row in enumerate(grid):
    for c, t in enumerate(row):
        if t == "S":
            print(max(walk(r, c).values()))
