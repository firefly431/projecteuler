from fractions import gcd

N = 1000

def sqrt2(x):
    "Generate square root convergents"
    num = 1
    den = 1
    for i in range(x):
        # n = 1 + 1 / (1 + n)
        # i0 = 1 + n
        # num += den
        # i1 = 1 / i0
        # num, den = den, num
        # i2 = 1 + i1
        # num += den
        # simplified:
        num,den=den+den+num,num+den
        # simplify fraction
        d = gcd(num, den)
        num //= d
        den //= d
        yield num, den

print(sum(1 for num, den in sqrt2(N) if len(str(num)) > len(str(den))))
