def seq(max):
    f1 = 1
    f2 = 1
    while f1 < max:
        f2 += f1
        f1 = f2 - f1
        yield f1

print(sum(x for x in seq(4000000) if x % 2 == 0))
