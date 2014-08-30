# this one seems fun
def hand(arr):
    cards = '23456789TJQKA'
    return [(cards.find(x[0]), x[1]) for x in arr]

def group(seq):
    import itertools
    return sorted([(k, len(list(g))) for k, g in itertools.groupby(seq)], key = lambda g: g[1])

def value(hand):
    # there are 10 hand types
    # but 13 possible cards
    # so we return rank * 16 * 16 * 16 * 16 * 16 * 16 + cards necessary for ranking
    # or (rank << 24) + high card
    # first, detect flush
    rmask = 24
    flush = all(hand[i][1] == hand[0][1] for i in range(1, len(hand)))
    hand = [x[0] for x in hand] # suit doesn't matter
    hand.sort()
    straight = False
    s = hand[0]
    if hand == [s, s + 1, s + 2, s + 3, s + 4]:
        straight = True
    if flush:
        if hand == [8, 9, 10, 11, 12]:
            return (10 << rmask) + 12
        if straight:
            return (9 << rmask) + s + 4
        return (6 << rmask) + (hand[0]) + (hand[1] << 4) + (hand[2] << 8) + (hand[3] << 12) + (hand[4] << 16)
    if straight:
        return (5 << rmask) + hand[-1]
    # detect multiples
    groups = group(hand)
    if groups[-1][1] == 4:
        return (8 << rmask) + (groups[-1][0] << 4) + (groups[0][0])
    if groups[-1][1] == 3:
        if groups[0][1] == 2:
            return (7 << rmask) + (groups[-1][0] << 4) + (groups[0][0])
        else:
            return (4 << rmask) + (groups[-1][0] << 8) + (groups[1][0] << 4) + (groups[0][0])
    if groups[-1][1] == 2:
        if groups[-2][1] == 2:
            return (3 << rmask) + (groups[-1][0] << 8) + (groups[1][0] << 4) + (groups[0][0])
        else:
            return (2 << rmask) + (groups[0][0]) + (groups[1][0] << 4) + (groups[2][0] << 8) + (groups[3][0] << 12)
    return (1 << rmask) + (hand[0]) + (hand[1] << 4) + (hand[2] << 8) + (hand[3] << 12) + (hand[4] << 16)

w1 = 0

with open('p054_poker.txt') as f:
    for line in f:
        s = line.split()
        a = s[:5]
        b = s[5:]
        if value(hand(a)) > value(hand(b)):
            w1 += 1

print(w1)
