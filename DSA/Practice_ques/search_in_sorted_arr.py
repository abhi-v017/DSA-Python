nums = [7,8,9,1,2,3,5,6]
target = 4
n = len(nums)
low = 0
high = n-1
while low<=high:
    mid = (low+high)//2
    if nums[mid]==target:
        print("True")
    if nums[mid]<=nums[high]:
        if nums[mid]<=target<=nums[high]:
            low = mid+1
        else:
            high = mid-1
    else:
        if nums[low]<=target<=nums[high]:
            high = mid-1
        else:
            low = mid+1
