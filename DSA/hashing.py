nums = [1,2,3,4,5,1,2,3,4,5,1,2,3,4,5]
n = len(nums)

# Using dictionary to count frequency of elements
freq_map = {}
for i in range (0, n):
    if nums[i] in freq_map:
        freq_map[nums[i]]+=1
    else:
        freq_map[nums[i]]=1
print(freq_map)

# Using get() method of dictionary to count frequency of elements
hash_map = {}
for i in range (0,n):
    hash_map[nums[i]] = hash_map.get(nums[i],0)+1
print(hash_map)
