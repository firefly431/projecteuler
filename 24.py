import itertools, number
print(''.join(str(x) for x in number.nth(itertools.permutations(range(10)), 1000000 - 1)))
