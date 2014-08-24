import math

from number import sigma

res = 0

for a in range(2, 10000):
    b = sigma(a) - a
    if b > a:
        if a == sigma(b) - b:
            res += a + b

print(res)
