def bubble_sort(nums):
    n = len(nums)
    for i in range(n-2, -1, -1):
        for j in range(0, i+1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums

nums = [1,4,6,4,8,2,0,7,5,9]  
print(bubble_sort(nums)) 

# time complexity = O(n^2)
# space complexity = O(1)