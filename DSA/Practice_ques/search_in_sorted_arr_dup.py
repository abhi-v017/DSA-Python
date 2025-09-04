nums = [7,7,7,7,8,9,1,2,3,5,6,7,7]
target = 5
n = len(nums)
low = 0
high = n-1
while low<=high:
    mid = (low+high)//2
    if nums[mid]==target:
        print("True")
    if nums[low]==nums[high]:
        low+=1
        high-=1
        continue
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
