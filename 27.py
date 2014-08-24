import primes, itertools

pcalc = 1000000

Pl = list(primes.sieve(pcalc))
P = set(Pl) # SERIOUS speedup
isprime = lambda x: ((primes.isprime(x)) if (x >= pcalc) else (x in P))

to_1000 = list(itertools.takewhile(lambda x: x < 1000, Pl))

longest = 0
l_a = 0
l_b = 0

lim = 1000

for a in range(-lim + 1, lim):
    for b in to_1000:
        if not isprime(longest * longest + a * longest + b): continue
        for i in itertools.count(1):
            if not isprime(i * i + a * i + b):
                if i + 1 > longest:
                    longest = i + 1
                    l_a = a
                    l_b = b
                break
    if a % 100 == 0:
        print("a = {:>5}, longest so far: ({:>5}, {:>5}) -> {:>5}".format(a, l_a, l_b, longest))

print(l_a * l_b)
