# check if diff. between adjacent numbers is greater than the smaller number for n >= 1
# if so, we can check numbers (1,1), (2,1), (2,2), (3,1)...(3,3), ...
# (triangularly)
# n(3n-1)/2-(n-1)(3n-2)/2 > 0 (?)
# (n(3n-1)-(n-1)(3n-2)) > 0 (?)
# (3n2-n-3n2+2n+3n-2) > 0 (?)
# (4n-2) > 0 (?)
# this is true for n > 1/2, so we can check triangularly

import itertools

def pent(x):
    import math
    a = 24 * x + 1
    sa = int(math.sqrt(a))
    return sa * sa == a and sa % 6 == 5

for a in itertools.count(2):
    pa = a * (3 * a - 1) // 2
    for b in range(a - 1, 0, -1):
        pb = b * (3 * b - 1) // 2
        if pent(pa + pb) and pent(pa - pb):
            print(pa - pb)
            break
    else:
        continue
    break
