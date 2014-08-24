def cyclen(den):
    rem = 1
    remd = {1: 0}
    i = 0
    while rem != 0:
        rem *= 10
        i += 1
        if rem > den:
            rem %= den
        if rem in remd:
            return i - remd[rem]
        remd[rem] = i
    return 0

print(max(range(7, 1000), key = cyclen))
