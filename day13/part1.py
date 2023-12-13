def ref(l):
    for i in range(1, len(l)):
        d = min(i, len(l) - i)
        a = l[i - d : i]
        b = l[i : i + d][::-1]
        if a == b:
            return i
    return 0

def solve(l):
    return 100 * ref(l) + ref(list(zip(*l)))

c = 0

for s in open(0).read().split("\n\n"):
    g = list(map(list, s.splitlines()))
    c += solve(g)

print(c)
