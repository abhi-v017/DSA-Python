nums = [0,3,12,4,56,0,45,0,50,0,5,3,4,4]
n=len(nums)
"""
temp = []
for i in range(0, n):
    if nums[i]!=0:
        temp.append(nums[i])

n2 = len(temp)
for i in range(0, n2):
    nums[i]=temp[i]

for i in range(n2, n):
    nums[i] = 0

print(nums)"""
    
for i in range(0, n):
    for j in range(i+1, n):
        if nums[j]==0:
            nums[i],nums[j]=nums[j],nums[i]
print(nums)