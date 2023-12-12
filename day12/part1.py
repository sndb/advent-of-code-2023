def arrangements(s):
    if len(s) == 0:
        return [""]
    if s[0] == "?":
        return [c + a for a in arrangements(s[1:]) for c in ".#"]
    return [s[0] + a for a in arrangements(s[1:])]


def groups(a):
    return [len(x) for x in a.split(".") if len(x) > 0]


total = 0

for l in open(0):
    x = l.split()
    s = x[0]
    g = [int(x) for x in x[1].split(",")]
    total += sum(g == groups(a) for a in arrangements(s))

print(total)
