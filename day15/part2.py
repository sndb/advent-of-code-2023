def hash(s):
    h = 0
    for c in s:
        h = (h + ord(c)) * 17 % 256
    return h

boxes = [[] for _ in range(256)]

for lens in open(0).read().strip().split(","):
    x = lens.split("=")
    if len(x) == 2:
        label = x[0]
        num = int(x[1])
        i = hash(label)
        for j in range(len(boxes[i])):
            if boxes[i][j][0] == label:
                boxes[i][j] = (label, num)
                break
        else:
            boxes[i].append((label, num))
    else:
        label = x[0][:-1]
        i = hash(label)
        boxes[i] = [(l, n) for l, n in boxes[i] if l != label]

total = 0

for i, box in enumerate(boxes):
    for j, lens in enumerate(box):
        total += (1 + i) * (1 + j) * lens[1]

print(total)
