nums = [-1,0,1,2,-1,-4]
my_set = set()

for i in range(0, len(nums)):
    for j in range(i+1, len(nums)):
        for k in range(j+1, len(nums)):
            if nums[i]+nums[j]+nums[k]==0:
                temp = [nums[i],nums[j],nums[k]]
                temp.sort()
                my_set.add(tuple(temp))
print(my_set)
#time complexity = O(n^3)

#better solutuion
result = set()
for i in range(0, len(nums)):
    my_set = set()
    for j in range(i+1, len(nums)):
        third = -(nums[i]+nums[j])
        if third in my_set:
            temp = [nums[i], nums[j], third]
            temp.sort()
            result.add(tuple(temp))
        my_set.add(nums[j])
print(result)
#time complexity = O(n^2)

#optimal solution
ans = []
n = len(nums)
nums.sort()
for i in range(0, n):
    if i!=0 and nums[i]==nums[i-1]:
        continue
    j = i+1
    k = n-1
    while j<k:
        total = nums[i]+nums[j]+nums[k]
        if total<0:
            j+=1
        elif total>0:
            k-=1
        else:
            temp = [nums[i], nums[j], nums[k]]
            ans.append(temp)
            j+=1
            k-=1
            #skip duplicates---------
            while j<k and nums[j] == nums[j-1]:
                j+=1
            while j<k and nums[k] == nums[k-1]:
                k-=1
print(ans)

#time somplexity = O(nlogn)+O(n^2)