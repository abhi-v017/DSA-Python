def remove_duplicate(nums):
    n = len(nums)
    if n == 0:
        return 0
    
    i = 0
    for j in range(1, n):
        if nums[i] != nums[j]:
            i += 1
            nums[i] = nums[j]
    
    return i + 1  # new length


nums = [1,1,2,2,3,3,4,4,5]
new_len = remove_duplicate(nums)
print(nums[:new_len])   # [1,2,3,4,5]
