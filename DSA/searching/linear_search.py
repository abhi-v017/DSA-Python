target = 4

nums = [1,2,3,4,5,6,7]

def linear_search(target, nums):
    n = len(nums)
    for i in range(0,n):
        if nums[i]==target:
            return i
    return -1
    
print(linear_search(target, nums))