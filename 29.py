import math, itertools
print(len(set(itertools.starmap(pow, itertools.product(range(2, 101), repeat = 2)))))
