import itertools
# first, find limit
# so sum of 5th powers of digits <= 9^5 * n
# with n = 10^n - 1
# so solve 9^5n = 10^n-1
# which occurs at 0 and a little before 6
# so only consider 1-6 digit numbers from 2...999999
print(sum(n for n in range(2, 1000000) if n == sum(int(ch)**5 for ch in str(n))))
