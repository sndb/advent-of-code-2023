from functools import cache

grid = open(0).read().splitlines()
dest = (140, 139)


def valid(r, c):
    return (
        r >= 0
        and r < len(grid)
        and c >= 0
        and c < len(grid[0])
        and grid[r][c] != "#"
    )


def adjacent(r, c):
    return [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]


@cache
def distance(p, q):
    queue = [(0, *p)]
    seen = set()
    p_neighbors = neighbors(*p)
    d_max = 0
    while queue:
        d, r, c = queue.pop()

        if (r, c) == q:
            d_max = max(d_max, d)

        if (r, c) in seen or (r, c) in p_neighbors:
            continue
        seen.add((r, c))

        for nr, nc in adjacent(r, c):
            if valid(nr, nc):
                queue.append((d + 1, nr, nc))
    return d_max


@cache
def neighbors(r0, c0):
    queue = [(r0, c0)]
    seen = set()
    res = []
    while queue:
        r, c = queue.pop()

        if (r, c) in seen:
            continue
        seen.add((r, c))

        if (r, c) == dest:
            res.append((r, c))
            continue

        passages = 0
        if (r, c) != (r0, c0):
            for nr, nc in adjacent(r, c):
                if valid(nr, nc):
                    passages += 1
        if passages >= 3:
            res.append((r, c))
            continue

        for nr, nc in adjacent(r, c):
            if valid(nr, nc) or (nr, nc) == dest:
                queue.append((nr, nc))
    return res


queue = [(0, 0, 1, tuple())]
answer = 0

while queue:
    d, r, c, path = queue.pop()

    if (r, c) == dest:
        answer = max(answer, d)
        continue

    if (r, c) in path:
        continue
    path += ((r, c),)

    for nr, nc in neighbors(r, c):
        nd = d + distance((r, c), (nr, nc))
        queue.append((nd, nr, nc, path))

print(answer)
