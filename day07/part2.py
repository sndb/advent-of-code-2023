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


def variants(hand):
    if len(hand) == 0:
        return [[]]
    if hand[0] != "J":
        return [[hand[0]] + v for v in variants(hand[1:])]
    return [[c] + v for v in variants(hand[1:]) for c in "23456789TQKA"]


def key(hand):
    t = max([typ(h) for h in variants(hand)])
    return tuple([t] + ["J23456789TQKA".index(c) for c in hand])


data = [l.split() for l in open(0)]
bids = [int(p[1]) for p in sorted(data, key=lambda p: key(p[0]))]
print(sum([(1 + i) * b for i, b in enumerate(bids)]))
