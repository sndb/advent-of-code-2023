def hash(s):
    h = 0
    for c in s:
        h = (h + ord(c)) * 17 % 256
    return h

total = 0

for x in open(0).read().strip().split(","):
    total += hash(x)

print(total)
