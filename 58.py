from itertools import count
from primes import isprime

n = 1
c = 0
for i in count(1, 2):
    n += i
    # skip bottom right (not actually diagonal)
    n += i
    c += isprime(n)
    i += 1
    n += i
    c += isprime(n)
    n += i
    c += isprime(n)
    # side length is i + 1
    # number of numbers is i * 2 + 1
    # c / (i * 2 - 1) < .1
    # so 10c < i * 2 - 1
    if 10 * c < i * 2 + 1:
        print(i + 1)
        break
