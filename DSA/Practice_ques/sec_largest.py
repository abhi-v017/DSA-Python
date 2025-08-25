nums = [1,45,34,-64,2,-32,-33,-43]
largest = nums[0]

for i in nums:
    largest = max(largest, i)

second_largest = nums[0]
for j in nums:
    if j<largest:
        second_largest = max(second_largest, j)

print(largest)
print(second_largest)