nums = [1,1,1,2,4,4,5,6,7,8,9,9,9]
target = 3
163
n = len(nums)
lb = n
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