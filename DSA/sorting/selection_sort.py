def selection_sort(nums):
    n = len(nums)
    for i in range(0, n):
        min_ind = i
        for j in range(i+1, n):
            if nums[j] < nums[min_ind]:
                min_ind = j
        nums[i], nums[min_ind] = nums[min_ind], nums[i]
    return nums
    
nums = [1,4,6,4,8,2,0,7,5,9]    
print(selection_sort(nums))

# time complexity = O(n^2)
# space complexity = O(1)