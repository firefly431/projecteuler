def lpf(num):
    import math
    while num & 1 == 0 and num > 1:
        num = num >> 1
    if num == 1:
        return 2
    fac = 3
    lfac = 1
    while fac < math.sqrt(num):
        if num % fac == 0:
            lfac = fac
            num = num // fac
        fac += 2
    return max((lfac, num))

print(lpf(600851475143))
