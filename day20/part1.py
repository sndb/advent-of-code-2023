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


high_sent = low_sent = 0


def propagate():
    global high_sent, low_sent

    queue = deque([(False, None, "broadcaster")])

    while queue:
        pulse, src, dst = queue.popleft()
        if pulse:
            high_sent += 1
        else:
            low_sent += 1

        mod = modules[dst]
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


for _ in range(1000):
    propagate()

print(high_sent * low_sent)
