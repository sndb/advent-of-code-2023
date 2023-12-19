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

parts = []

for line in data[1].splitlines():
    part = [int(s.split("=")[1]) for s in line[1:-1].split(",")]
    parts.append(tuple(part))


def process(wf, part):
    if wf == "A":
        return sum(part)
    if wf == "R":
        return 0
    for step in workflows[wf]:
        if type(step) == str:
            return process(step, part)
        cat, op, num, nwf = step
        if op == "<" and part[cat] < num:
            return process(nwf, part)
        if op == ">" and part[cat] > num:
            return process(nwf, part)


total = 0

for part in parts:
    total += process("in", part)

print(total)
