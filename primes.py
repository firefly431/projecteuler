# util module to generate primes up to a number

def sieve(limit):
    s = [False, False, True] + [True, False] * ((limit - 1) >> 1)
    # 2 already filtered out
    for i, ok in enumerate(s):
        if not ok: continue
        for n in range(i * i, limit + 1, 2 * i):
            s[n] = False
        yield i

def isprime(n):
    import math
    if n < 2: return False
    if n == 2: return True
    if n & 1 == 0: return False
    for i in range(3, int(math.sqrt(n)) + 2, 2):
        if n % i == 0 and i < n:
            return False
    return True

def primes(precomp = 100): # generator
    # precompute a few primes
    oldp = list(sieve(precomp))
    n = 0
    for p in oldp:
        yield p
        n = p
    while True:
        n += 2
        valid = True
        for p in oldp:
            if p * p > n:
                break
            if n % p == 0:
                valid = False
                break
        if not valid: continue
        yield n
        oldp.append(n)

if __name__ == "__main__":
    import sys
    a = 100
    if len(sys.argv) > 1:
        a = int(sys.argv[1])
    print(list(sieve(a)))
