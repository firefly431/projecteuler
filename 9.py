
# the smallest numbers that satisfy a < b < c are a, a + 1, a + 2
# so max(a) = (solution to 3a + 3 = n) = (n - 1) / 3
# the smallest numbers that satisfy a < b < c are a, b, b + 1
# if a < b
# so max(b) = (solution to a + 2b + 1 = n) = (n - a - 1) / 2
def triplets(n):
    for a in range(1, (n - 1) // 3 + 2):
        for b in range(a + 1, (n - a) // 2):
            yield (a, b, n - a - b)

pyth_ = lambda a, b, c: a * a + b * b == c * c
# lazy
pyth = lambda t: pyth_(*t)

triplet = next(filter(pyth, triplets(1000)))

a, b, c = triplet
print(a * b * c)

