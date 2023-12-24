import sys

sys.setrecursionlimit(10000)

grid = open(0).read().splitlines()
seen = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
dest = (140, 139)
answer = 0


def dfs(r, c, d):
    global answer

    if (r, c) == dest:
        answer = max(answer, d)
        return

    if seen[r][c]:
        return

    seen[r][c] = True

    if grid[r][c] == ">":
        dfs(r, c + 1, d + 1)
    elif grid[r][c] == "v":
        dfs(r + 1, c, d + 1)
    else:
        for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
            if (
                nr >= 0
                and nr < len(grid)
                and nc >= 0
                and nc < len(grid[0])
                and grid[nr][nc] != "#"
            ):
                dfs(nr, nc, d + 1)

    seen[r][c] = False


dfs(0, 1, 0)
print(answer)
