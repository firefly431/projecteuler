# quite slow
# a + b + c = p
# a^2 + b^2 = c^2
# a + b + sqrt(a^2 + b^2) = p
# b < 1/2 p - 1
# a < b

maxn = 0

for p in range(12, 1001):
    ntrips = 0
    for b in range(4, p // 2 - 1):
        for a in range(3, b):
            c = p - a - b
            if c * c == a * a + b * b:
                ntrips += 1
    if ntrips > maxn:
        maxn = ntrips
        print(p, maxn)
