from itertools import groupby


def ref(l):
    for i in range(1, len(l)):
        d = min(i, len(l) - i)
        a = l[i - d : i]
        b = l[i : i + d]
        if a == list(reversed(b)):
            return i
    return 0


def solve(l):
    return 100 * ref(l) + ref(list(zip(*l)))


c = 0

for k, g in groupby(open(0).read().splitlines(), bool):
    if k:
        c += solve(list(map(list, g)))

print(c)
