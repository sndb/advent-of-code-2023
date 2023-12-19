data = open(0).read().split("\n\n")

workflows = {}

for line in data[0].splitlines():
    name, rules = line[:-1].split("{")
    wf = []
    for rule in rules.split(","):
        s = rule.split(":")
        if len(s) == 1:
            wf.append(s[0])
        else:
            test, nwf = s
            cat = "xmas".index(test[0])
            op = test[1]
            num = int(test[2:])
            wf.append((cat, op, num, nwf))
    workflows[name] = wf


def cut(op, rs, i, j):
    pre, r, suf = rs[:i], rs[i], rs[i + 1 :]
    if op == "<":
        xs = [(r[0], j - 1), (j, r[1])]
    else:
        xs = [(j + 1, r[1]), (r[0], j)]
    return [pre + (x,) + suf for x in xs]


def process(wf, rs):
    if wf == "A":
        n = 1
        for r in rs:
            n *= r[1] - r[0] + 1
        return n
    if wf == "R":
        return 0
    acc = 0
    for rule in workflows[wf]:
        if type(rule) == str:
            return acc + process(rule, rs)
        cat, op, num, nwf = rule
        nrs, rs = cut(op, rs, cat, num)
        acc += process(nwf, nrs)
    return acc


print(process("in", 4 * ((1, 4000),)))
