nums = [1,2,3,4,5,6,7,9,8]
target = 12

def two_sum(nums, target):
    for i in range(0, len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i]+nums[j]==target and nums[i]!=nums[j]:
                return [i,j]
            
def two_sum_dict(nums, target):
    hash_map = {}
    for i in range(0, len(nums)):
        remaining = target - nums[i]
        if remaining in hash_map:
            return [hash_map[remaining], i]
        hash_map[nums[i]] = i

print(two_sum(nums, target)) 
print(two_sum_dict(nums, target))