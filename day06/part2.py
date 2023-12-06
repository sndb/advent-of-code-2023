t, d = [int("".join(l.split()[1:])) for l in open(0)]

n = 0

for v in range(1, t):
    if (t - v) * v > d:
        n += 1

print(n)
