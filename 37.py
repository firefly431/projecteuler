# generate some primes
import primes
Pl = primes.sieve(1000000)
P = set(Pl)
def isprime(p):
    if p < 1000000:
        return p in Pl
    else:
        return primes.isprime(p)

