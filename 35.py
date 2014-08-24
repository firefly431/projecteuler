import primes, math
P = set(primes.sieve(1000000))
n = 0
for p in P:
    o = p
    ndigs10 = 10**int(math.log10(o))
    while p in P:
        p = p // 10 + (p % 10) * ndigs10
        if p == o:
            n += 1
            break
print(n)
