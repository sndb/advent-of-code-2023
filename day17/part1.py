from collections import defaultdict, deque

grid = [list(map(int, l)) for l in open(0).read().splitlines()]


def walk(src, dst):
    costs = defaultdict(lambda: float("inf"))
    queue = deque([(src, (0, 0), 0, 0)])
    res = float("inf")
    while queue:
        curr, prev, run, cost = queue.pop()
        if run > 3:
            continue

        k = (curr, prev, run)
        if costs[k] <= cost:
            continue
        costs[k] = cost

        if curr == dst and cost < res:
            res = cost
            continue

        dprev = (curr[0] - prev[0], curr[1] - prev[1])
        for dsucc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            succ = (curr[0] + dsucc[0], curr[1] + dsucc[1])
            if succ == prev:
                continue
            if succ[0] < 0 or succ[0] >= len(grid):
                continue
            if succ[1] < 0 or succ[1] >= len(grid[0]):
                continue
            csucc = cost + grid[succ[0]][succ[1]]
            rsucc = 1 + (run if dsucc == dprev else 0)
            queue.appendleft((succ, curr, rsucc, csucc))
    return res


print(walk((0, 0), (len(grid) - 1, len(grid[0]) - 1)))
