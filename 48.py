def mod_pow(b, e, m): # binary exponentiation
    r = 1
    b = b % m
    while e > 0:
        if (e & 1 == 1):
            r = (r * b) % m
        e = e >> 1
        b = (b * b) % m
    return r

last10 = 10**10

r = 0

for i in range(1, 1000 + 1):
    r += mod_pow(i, i, last10)
    r = r % last10

print(r)
