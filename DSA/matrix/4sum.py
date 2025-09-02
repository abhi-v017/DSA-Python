nums = [-1,0,1,3,2,-1,-4,2,-4,-1,-3]
my_set = set()

for i in range(0, len(nums)):
    for j in range(i+1, len(nums)):
        for k in range(j+1, len(nums)):
            for l in range(k+1, len(nums)):
                if nums[i]+nums[j]+nums[k]+nums[l]==0:
                    temp = [nums[i],nums[j],nums[k],nums[l]]
                    temp.sort()
                    my_set.add(tuple(temp))
print(my_set)

#better solution
result = set()
for i in range(0, len(nums)):
    for j in range(i+1, len(nums)):
        my_set = set()
        for k in range(j+1, len(nums)):
            fourth = -(nums[i]+nums[j]+nums[k])
            if fourth in my_set:
                temp = [nums[i], nums[j], nums[k], fourth]
                temp.sort()
                result.add(tuple(temp))
            my_set.add(nums[j])
print(result)

#optimal solution
ans = []
n = len(nums)
nums.sort()
for i in range(0, n):
    if i!=0 and nums[i]==nums[i-1]:
        continue
    for j in range(i+1, n):
        if j>i+1 and nums[j]==nums[j-1]:
            continue
        k = j+1
        l = n-1
        while k<l:
            total = nums[i]+nums[j]+nums[k]+nums[l]
            if total<0:
                k+=1
            elif total>0:
                l-=1
            else:
                temp = [nums[i], nums[j], nums[k], nums[l]]
                ans.append(temp)
                k+=1
                l-=1
                #skip duplicates---------
                while k<l and nums[k] == nums[k-1]:
                    k+=1
                while k<l and nums[l] == nums[l-1]:
                    l-=1
print(ans)