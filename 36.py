# if it's < 1 million, has at most 6 digits
# consider the first part (at most 3 digits): ABC
# there are two palindromes: ABCBA and ABCCBA
# since it can't have leading zeros in binary
# it must be odd
total = 0
def isbpal(x):
    bs = bin(x)[2:]
    return x & 1 == 1 and bs[::-1] == bs
def consider(x):
    global total
    if isbpal(x):
        total += x
for fp in range(1, 1000):
    sfp = str(fp)
    p1 = int(sfp + sfp[::-1])
    p2 = int(sfp + sfp[-2::-1])
    consider(p1)
    consider(p2)

print(total)
