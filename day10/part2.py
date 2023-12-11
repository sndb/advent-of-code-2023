grid = open(0).read().splitlines()


def adj(r, c):
    match grid[r][c]:
        case "|":
            return [(r - 1, c), (r + 1, c)]
        case "-" | "S":
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
    dists = {}
    queue = [(r, c, 0)]
    while len(queue) > 0:
        r, c, d = queue.pop()
        if d < dists.get((r, c), float("inf")):
            dists[r, c] = d
            for ar, ac in adj(r, c):
                queue.append((ar, ac, d + 1))
    return dists


def area(loop):
    a = 0
    for r in range(len(grid)):
        inside = False
        for c in range(len(grid[0])):
            if (r, c) in loop and grid[r][c] in "|LJ":
                inside = not inside
            if (r, c) not in loop and inside:
                a += 1
    return a


for r in range(len(grid)):
    for c in range(len(grid[0])):
        if grid[r][c] == "S":
            print(area(walk(r, c).keys()))
