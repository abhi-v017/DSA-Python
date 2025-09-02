nums = [1,2,3,98,99,100,101,4]
n = len(nums)
max_count = 0

for i in range(0, n):
    num = nums[i]
    count = 1
    while num+1 in nums:
        count+=1
        num+=1
    max_count = max(count, max_count)
    
print(max_count)
#time complexity = O(n^2)

#optimal solution--------
my_set = set(nums)

n = len(nums)
longest = 0
for num in my_set:
    if num-1 not in my_set:
        count=1
        while num+1 in my_set:
            count+=1
            num+=1
        longest = max(longest, count)
        
print(longest)
print(nums)

#time complexity = O(n+n+n) => O(3n) => O(n)