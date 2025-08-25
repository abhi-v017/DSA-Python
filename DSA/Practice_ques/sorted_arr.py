nums = [1,2,3,4,5,6]
nums2 = [1,4,5,2,3,5,7,9,3]

def isarrsorted(nums):
    n= len(nums)
    for i in range(0, n-1):
        if nums[i] > nums[i+1]:
            return False
    return True

print(isarrsorted(nums))