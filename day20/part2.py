from math import lcm
from collections import deque

modules = {}

for line in open(0).read().splitlines():
    mod, out = line.split(" -> ")
    out = out.split(", ")

    if mod == "broadcaster":
        modules[mod] = {"typ": None, "out": out}
        continue

    typ, mod = mod[0], mod[1:]
    if "rx" in out:
        modules["rx"] = {"typ": None, "in": mod, "out": []}
    if typ == "%":
        modules[mod] = {"typ": typ, "on": False, "out": out}
    else:
        modules[mod] = {"typ": typ, "in": {}, "out": out}

for name, mod in modules.items():
    for out in mod["out"]:
        if modules[out]["typ"] == "&":
            modules[out]["in"][name] = False


button_presses = 0
result = {}


def propagate():
    global result, button_presses
    button_presses += 1

    queue = deque([(False, None, "broadcaster")])

    while queue:
        pulse, src, dst = queue.popleft()
        mod = modules[dst]

        if dst == modules["rx"]["in"]:
            for k, v in mod["in"].items():
                if k not in result:
                    result[k] = 0
                if v:
                    result[k] = button_presses

        if mod["typ"] == "%":
            if not pulse:
                send = mod["on"] = not mod["on"]
                for out in mod["out"]:
                    queue.append((send, dst, out))
        elif mod["typ"] == "&":
            mod["in"][src] = pulse
            send = not all(mod["in"].values())
            for out in mod["out"]:
                queue.append((send, dst, out))
        else:
            for out in mod["out"]:
                queue.append((False, dst, out))


while True:
    propagate()
    if all(result.values()):
        print(lcm(*result.values()))
        break
