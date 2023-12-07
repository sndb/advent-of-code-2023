def typ(hand):
    x = sorted([hand.count(c) for c in set(hand)])
    r = [
        [1, 1, 1, 1, 1],
        [1, 1, 1, 2],
        [1, 2, 2],
        [1, 1, 3],
        [2, 3],
        [1, 4],
        [5],
    ]
    return r.index(x)


def key(hand):
    return tuple([typ(hand)] + ["23456789TJQKA".index(c) for c in hand])


data = [l.split() for l in open(0)]
bids = [int(p[1]) for p in sorted(data, key=lambda p: key(p[0]))]
print(sum([(1 + i) * b for i, b in enumerate(bids)]))
