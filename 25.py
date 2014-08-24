import itertools
import number

print(next(itertools.dropwhile(lambda x: len(str(x[1])) < 1000, enumerate(number.fib())))[0])
