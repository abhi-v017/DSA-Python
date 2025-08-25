def partition(nums, low, high):
    pivot = nums[low]
    i,j= low, high
    while i<j:
        while nums[i]<=pivot and i<=high-1:
            i+=1
        while nums[j]>pivot and j>=low+1:
            j-=1
        if i<j:
            nums[i],nums[j]=nums[j],nums[i]
    nums[low], nums[j]=nums[j], nums[low]
    return j
def quick_sort(nums,low, high):
    if low<high:
        p_ind = partition(nums, low, high)
        quick_sort(nums, low, p_ind-1)
        quick_sort(nums, p_ind+1, high)
    return nums

arr = [7, 2, 1, 6, 8, 5, 3, 4]
print(quick_sort(arr, 0, len(arr) - 1))


# time complexity = O(nlogn)
# space complexity = O(1)