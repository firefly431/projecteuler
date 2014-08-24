import itertools, fractions

num = 1
dem = 1

def consider(aa, bb, a, b):
    global num, dem
    if aa / bb == a / b:
        num *= a
        dem *= b

p2 = list(itertools.combinations(range(1, 10), 2))

for comdig in range(1, 10):
    for a, b in p2:
        consider(a * 10 + comdig, b * 10 + comdig, a, b)
        consider(a * 10 + comdig, comdig * 10 + b, a, b)
        consider(comdig * 10 + a, b * 10 + comdig, a, b)
        consider(comdig * 10 + a, comdig * 10 + b, a, b)

print(dem // fractions.gcd(num, dem))
