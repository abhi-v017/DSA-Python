# smallest index such that nums[i]>=target
nums = [1,1,1,2,4,4,5,6,7,8,9,9,9]
target = 1
n = len(nums)
# lower bound
lb = -1
low = 0
high = n-1
while low<=high:
    mid = (low+high)//2
    if nums[mid]>=target:
        lb = mid
        high = mid-1
    else:
        low = mid+1
print(lb)

# upper bound
ub = n
low = 0
high = n-1
while low<=high:
    mid = (low+high)//2
    if nums[mid]>target:
        ub = mid
        high = mid-1
    else:
        low = mid+1
print(ub)

