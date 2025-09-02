nums = [1,2,-3,4,-5,-6,8]
n = len(nums)
result = [0]*n
neg = 1
pos = 0

for i in range(0, n):
    if nums[i]>=0:
        result[pos] = nums[i]
        pos+=2
    else:
        result[neg] = nums[i]
        neg+=2
    
print(nums)
print(result)