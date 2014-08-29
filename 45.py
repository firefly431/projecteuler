import itertools, number

for i in itertools.count(144):
    if number.pent(i * (2 * i - 1)):
        print(i * (2 * i - 1))
        break
