s = '0'
i = 1
while len(s) < 1000001:
    s += str(i)
    i += 1
def d(x):
    return int(s[x])
r = 1
for j in range(7):
    r *= d(10 ** j)
print(r)
