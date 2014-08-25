import primes
import itertools
import sys
for i in reversed(range(1, 10)):
    for perm in itertools.permutations(reversed('123456789'[:i])):
        perm = ''.join(perm)
        if primes.isprime(int(perm)):
            print(perm)
            sys.exit(0)
