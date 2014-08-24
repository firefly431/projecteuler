# the product of an a-digit and b-digit number has at least (a + b - 1) digits
# and at most (a + b) digits
# thus if a + b + a + b (- 1)? = 9,
# 2a + 2b is 9 or 10
# thus a + b must equal 5
import math, itertools
products = set()
for a in range(1, 100000):
    astr = str(a)
    A = len(astr)
    B = 5 - A
    for b in range(int(10 ** (B - 1)), int(10 ** B)):
        c = a * b
        allstr = astr + str(b) + str(c)
        if ''.join(list(sorted(allstr))) == '123456789':
            products.add(c)

print(sum(products))
