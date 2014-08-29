import number, itertools

def nfacs(n):
    return sum(1 for _ in number.pfactor(n))

i = 1
while True:
    if nfacs(i) >= 4:
        if nfacs(i + 1) >= 4:
            if nfacs(i + 2) >= 4:
                if nfacs(i + 3) >= 4:
                    print(i)
                    break
                else:
                    i += 4
                    continue
            else:
                i += 3
                continue
        else:
            i += 2
            continue
    else:
        i += 1
        continue
