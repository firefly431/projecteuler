# plotting in wolframalpha, we get that the n < 1778280
facs = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]
print(sum(n for n in range(3, 1778280) if n == sum(facs[int(i)] for i in str(n))))
