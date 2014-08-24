# generate some primes
import primes
Pl = list(primes.sieve(1000000))
P = set(Pl)
def isprime(p):
    if p < 1000000:
        return p in Pl
    else:
        return primes.isprime(p)

# generate primes truncatable from right
queue = list(primes.sieve(10))
result = []

def ltrunc(x):
    import math
    highest = 10**int(math.log10(x))
    while x > 0:
        x = x % highest
        highest = highest // 10
        if x > 0 and not isprime(x):
            return False
    return True

while len(result) < 11:
    nqueue = []
    for p in queue:
        p *= 10
        for d in (1, 3, 7, 9): # cannot be even or end in 5
            np = p + d
            if isprime(np):
                if ltrunc(np):
                    result.append(np)
                nqueue.append(np)
        queue = nqueue
    if not queue:
        print("Error, ran out of primes")
        break
print(sum(result))
