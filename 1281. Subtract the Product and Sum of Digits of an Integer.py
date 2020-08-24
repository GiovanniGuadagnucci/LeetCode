import math

n = 234
n = str(n)
nums = list()
for i in n:
    nums.append(int(i))
print(nums)
return math.prod(nums) - sum(nums)

