def extrapolate(s):
    if len(set(s)) == 0:
        return 0
    t = [s[i + 1] - s[i] for i in range(len(s) - 1)]
    e = extrapolate(t)
    return s[-1] + e


data = [[int(x) for x in l.split()] for l in open(0)]
print(sum([extrapolate(s) for s in data]))
