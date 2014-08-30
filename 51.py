import primes
import itertools
import sys

Pl = primes.precomp(1000000)

i = 0

for p in Pl:
    i = i + 1
    if p == 121313:
        print(p)
    s = str(p)
    for a in '012':
        nn = 10
        fam = []
        for b in '0123456789':
            rr = s.replace(a, b)
            if rr[0] == '0': break
            if rr == s and a != b: break
            if not primes.isprime(int(rr)):
                nn -= 1
                if nn < 8:
                    break
            else:
                fam.append(int(rr))
        else:
            print(p)
            print(fam)
            sys.exit(0)
