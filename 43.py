import itertools
divs = (2, 3, 5, 7, 11, 13, 17)
total = 0
for n in itertools.permutations('0123456789'):
    n = ''.join(n)
    for i in range(1, 8):
        if int(n[i:i+3]) % divs[i - 1] != 0:
            break
    else:
        total += int(n)

print(total)
