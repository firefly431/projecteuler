import primes, number

P = list(primes.sieve(10000))

def isprime(n):
    if n <= max(P):
        return n in P
    return primes.isprime(n)

def prime(skip2 = False): # generator
    global P
    n = 0
    for p in P:
        if p == 2 and skip2: continue
        yield p
        n = p
    while True:
        n += 2
        valid = True
        for p in P:
            if p * p > n:
                break
            if n % p == 0:
                valid = False
                break
        if not valid: continue
        yield n
        P.append(n)

def until(gen, pred):
    for i in gen:
        if pred(i):
            break
        yield i

import itertools

for i in itertools.count(35, 2):
    if isprime(i): continue
    for p in until(prime(True), lambda x: x >= i):
        j = (i - p) // 2
        if number.square(j):
            break
    else:
        print(i)
        break

