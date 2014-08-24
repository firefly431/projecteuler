# quite slow

import math

from number import sigma

abundant = []
for i in range(2, 28123):
    if sigma(i) - i > i:
        abundant.append(i)

nums = list([False] * 28123)

for i, a in enumerate(abundant):
    for j in range(i + 1):
        b = abundant[j]
        if a + b < len(nums):
            nums[a + b] = True

print(sum(i for i, _ in enumerate(nums) if not _))
