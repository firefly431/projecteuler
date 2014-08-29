import itertools, primes

P = set(x for x in primes.sieve(10000) if x >= 1000)


for i in P:
    if i == 1487: continue
    s = ''.join(sorted(str(i)))
    perms = [x for x in P if ''.join(sorted(str(x))) == s and x != i]
    if len(perms) == 0: continue
    for j in perms:
        if (2 * j - i) in perms:
            print(str(i) + str(j) + str(2 * j - i))
            break
    else: continue
    break
