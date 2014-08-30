# for each factor in B!, there exists one term in A!/(A-B)! that divides it.

def prod(seq):
    import functools, operator
    return functools.reduce(operator.mul, seq)

# must use an algorithm as combinations
# can get REALLY big
def Cmil(n, r): # is nCr > 1000000
    if r * 2 > n:
        return Cmil(n, n - r)
    rf = list(range(1, r + 1))
    p = 1
    for f in range(n - r + 1, n + 1):
        remain = []
        for rff in rf:
            if f % rff == 0:
                f /= rff
            else:
                remain.append(rff)
        rf = remain
        p *= f
        if p > 1000000:
            ap = p
            for rff in rf:
                ap //= rff
                if ap <= 1000000:
                    break
            else:
                return True
    return False

t = 0
for n in range(1, 100 + 1):
    for r in range(0, n + 1):
        if Cmil(n, r):
            t += 1
print(t)
