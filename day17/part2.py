from heapq import heappop, heappush

grid = [list(map(int, l)) for l in open(0).read().splitlines()]
queue = [(0, 0, 0, 0, 0, 0)]
seen = set()

while queue:
    w, r, c, dr, dc, n = heappop(queue)

    if (r, c) == (len(grid) - 1, len(grid[0]) - 1) and n >= 4:
        print(w)
        break

    if (r, c, dr, dc, n) in seen:
        continue
    seen.add((r, c, dr, dc, n))

    for ndr, ndc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nr, nc = r + ndr, c + ndc
        if nr < 0 or nr >= len(grid) or nc < 0 or nc >= len(grid[0]):
            continue

        nw = w + grid[nr][nc]
        if (dr, dc) == (ndr, ndc):
            if n < 10:
                heappush(queue, (nw, nr, nc, ndr, ndc, n + 1))
        elif n >= 4 and (-dr, -dc) != (ndr, ndc) or (dr, dc) == (0, 0):
            heappush(queue, (nw, nr, nc, ndr, ndc, 1))
