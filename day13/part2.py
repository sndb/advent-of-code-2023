from itertools import groupby


def ref(l):
    r = []
    for i in range(1, len(l)):
        d = min(i, len(l) - i)
        a = l[i - d : i]
        b = l[i : i + d]
        if a == list(reversed(b)):
            r.append(i)
    return r


def solve(l):
    h = ref(l)
    v = ref(list(zip(*l)))
    for r in range(len(l)):
        for c in range(len(l[0])):
            x = l[r][c]
            l[r][c] = "#" if x == "." else "."
            for i in ref(l):
                if i not in h:
                    return 100 * i
            for i in ref(list(zip(*l))):
                if i not in v:
                    return i
            l[r][c] = x


c = 0

for k, g in groupby(open(0).read().splitlines(), bool):
    if k:
        c += solve(list(map(list, g)))

print(c)
