data = [[int(x) for x in l.split()[1:]] for l in open(0)]

n = 1

for t, d in zip(*data):
    c = 0
    for v in range(1, t):
        if (t - v) * v > d:
            c += 1
    n *= c

print(n)
