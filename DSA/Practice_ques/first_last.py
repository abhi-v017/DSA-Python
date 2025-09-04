nums = [1,1,1,2,4,4,5,6,7,8,9,9,9]
target = 4
n = len(nums)

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

ub = lb
low = 0
high = n-1
while low<=high:
    mid = (low+high)//2
    if nums[mid]>target:
        ub = mid
        high = mid-1
    else:
        low = mid+1
print([lb,ub])