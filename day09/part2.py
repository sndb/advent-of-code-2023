data = [[int(x) for x in l.split()] for l in open(0)]


def next_seq(s):
    return [s[i + 1] - s[i] for i in range(len(s) - 1)]


def extrapolate(s):
    if set(s) == {0}:
        return s + [0]
    e = extrapolate(next_seq(s))
    t = s[-1] + e[-1]
    return s + [t]


a = 0

for s in data:
    e = extrapolate(s[::-1])
    a += e[-1]

print(a)
