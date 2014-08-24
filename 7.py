def nth(seq, n, default = None):
    import itertools
    return next(itertools.islice(seq, n - 1, None), default)

import itertools
import primes
print(nth((x for x in itertools.count(1) if primes.isprime(x)), 10001))
