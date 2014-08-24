import primes
import math
import itertools

pcalc = 100

from number import tau

# consider pairs (a, b) = (1, 2), (3, 4), (5, 6)...
# tri. numbers are a * (b / 2), (b / 2) * (a + 2)...
# also tau(#) = tau(a) * tau(b / 2), tau(b / 2) * tau(a + 2)
# since they are relatively prime

for a in itertools.count(1, 2):
    b = a + 1
    tauA = tau(a)
    tauB = tau(b // 2)
    tauC = tau(a + 2)
    if tauA * tauB > 500:
        print(a * b // 2)
        break
    elif tauB * tauC > 500:
        print(b * c // 2)
        break
