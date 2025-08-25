nums = [1,4,6,4,8,2,0,7,5,9]  

def insrtion_sort(nums):
    n = len(nums)
    for i in range(1,n):
        key = nums[i]
        j = i-1
        while j>=0 and nums[j]>key:
            nums[j+1] = nums[j]
            j-=1
        nums[j+1] = key
    return nums


print(insrtion_sort(nums))

# time complexity = O(n^2)
# space complexity = O(1)
