nums = [7,8,9,2,3,5]
mini = float("inf")
n = len(nums)
low = 0
high = n-1

while low<=high:
    mid = (low+high)//2
    if nums[mid]<=high:
        mini = min(mini,nums[mid])
        high = mid-1
    else:
        mini = min(mini,nums[low])
        low = mid+1
print(mini)