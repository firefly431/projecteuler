def same(a, b):
    return ''.join(sorted(str(a))) == ''.join(sorted(str(b)))

def all_same(l):
    for i in range(1, len(l)):
        if not same(l[i - 1], l[i]): break
    else: return True
    return False

i = 0
while True:
    i += 1
    if all_same((i * 2, i * 3, i * 4, i * 5, i * 6)):
        print(i)
        break
