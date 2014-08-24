cmap = [None] * 1000000

i = 0
while True:
    n = 1 << i
    if n >= len(cmap):
        break
    cmap[n] = i + 1
    i += 1

def collatzlength(n):
    global cmap
    if n >= len(cmap):
        if n & 1 == 0:
            return collatzlength(n // 2) + 1
        else:
            return collatzlength((3 * n + 1) // 2) + 2
    if cmap[n] == None:
        if n & 1 == 0:
            cmap[n] = collatzlength(n // 2) + 1
        else:
            cmap[n] = collatzlength((3 * n + 1) // 2) + 2
    return cmap[n]

print(max(range(1, 1000000 + 1), key = collatzlength))
