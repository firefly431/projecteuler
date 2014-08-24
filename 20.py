fac100 = 1
for i in range(2, 101):
    fac100 *= i
print(sum(int(x) for x in str(fac100)))
