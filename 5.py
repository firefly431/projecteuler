import primes

# find LCM of any nums
nums = list(range(1, 21))

res = 1

def divideout(n):
    global nums
    ret = False
    for i in range(len(nums)):
        if nums[i] % n == 0:
            nums[i] = nums[i] // n
            ret = True
    return ret

for p in primes.sieve(max(nums)):
    while divideout(p): res *= p

print(res)
