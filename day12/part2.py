from functools import cache


@cache
def arrangements(s, g):
    if not g:
        return set(s) <= set(".?")
    if sum(g) + len(g) - 1 > len(s):
        return 0
    r = g[0]
    if set(s[:r]) <= set("#?") and (r >= len(s) or s[r] in ".?"):
        a1 = arrangements(s[r + 1 :], g[1:])
        a2 = s[0] in ".?" and arrangements(s[1:], g)
        return a1 + a2
    return s[0] != "#" and arrangements(s[1:], g)


total = 0

for l in open(0):
    x = l.split()
    s = "?".join(5 * [x[0]])
    g = 5 * tuple(map(int, x[1].split(",")))
    total += arrangements(s, g)

print(total)
