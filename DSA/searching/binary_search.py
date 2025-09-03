nums = [1,2,4,5,7,8,9,10]  #sorted
target = 4
# iterative method preffered
def binary_search(nums, target):
    n = len(nums)
    low = 0
    high = n-1
    while low<=high:
        mid = (low+high)//2
        if nums[mid]==target:
            return mid
        elif nums[mid]>target:
            high = mid-1
        else:
            low = mid+1
print(binary_search(nums, target))

# recursive method
n = len(nums)
low = 0
high = n-1
def recursive_binary_search(nums, low, high, target):
    if low>high:
        return -1
    mid = (low+high)//2
    if nums[mid]==target:
        return mid
    elif nums[mid]>target:
        return recursive_binary_search(nums,low,mid-1,target)
    else:
        return recursive_binary_search(nums,mid+1,high,target)

print(recursive_binary_search(nums,low,high,target))