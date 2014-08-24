# since n > 1, the int must be 4 digits (cannot be 5)
# not too many cases, only ~100000
import math
def pans():
    for i in range(1, 10000):
        s = ''
        n = 1
        while len(s) < 9:
            s += str(i * n)
            n += 1
        if ''.join(sorted(s)) == '123456789':
            yield int(s)
print(max(pans()))
