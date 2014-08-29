# preliminary tests indicate that for the sum of primes to be less than a million,
# there can only be at most 547 primes

import primes, sys

Pl = list(primes.sieve(1000000))
P  = set(Pl)

for l in range(547, 1, -1):
    if l % 1000 == 0:
        print("Testing " + str(l))
    for i in range(len(Pl) - l + 1):
        s = sum(Pl[i:i+l])
        if s >= 1000000:
            break
        if s in P:
            print(s)
            sys.exit(0)
