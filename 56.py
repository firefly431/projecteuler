import itertools, operator
print(max(map(lambda x: sum(map(int, str(x))),itertools.starmap(operator.pow, itertools.product(range(1, 101), range(1, 101))))))
