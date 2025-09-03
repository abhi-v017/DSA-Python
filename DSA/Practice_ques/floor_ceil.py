nums = [3,3,4,4,5,6,6,7,7,9,9,11,12,13,14]
target = 1
n = len(nums)
floor = -1
ceil = -1
low = 0
high = n-1
while low<high:
    mid = (low+high)//2
    if nums[mid]==target:
        print([nums[mid],nums[mid]])
    elif nums[mid]>target:
        ceil = nums[mid]
        high = mid-1
    else:
        floor = nums[mid]
        low = mid+1

print([floor, ceil])
