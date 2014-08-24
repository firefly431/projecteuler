def pals():
    for n1 in range(100, 1000):
        for n2 in range(n1, 1000):
            prod = n1 * n2
            if str(prod) == str(prod)[::-1]:
                yield prod

print(max(pals()))
