def is_lychrel(x):
    for iter in range(50):
        sx = str(x)
        rsx = sx[::-1]
        if rsx == sx and iter > 0: return False
        x = int(sx) + int(sx[::-1])
    return True

print(len(list(filter(is_lychrel, range(10000)))))
