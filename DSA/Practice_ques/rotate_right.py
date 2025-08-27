nums = [1,2,3,4,5,6,7]
n = len(nums)
temp = nums[n-1]

for i in range(n-2, -1, -1):
    nums[i+1] = nums[i]
nums[0] = temp

print(nums)


term = int(input("Enter number of terms: "))
for i in range(1,term+1):
    temp = nums[n-1]

    for i in range(n-2, -1, -1):
        nums[i+1] = nums[i]
    nums[0] = temp

print(nums)