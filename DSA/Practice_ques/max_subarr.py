nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
maxi = float("-inf")
for i in range(0, len(nums)):
    total = 0
    for j in range(i, len(nums)):
        total = total + nums[j]
        maxi = max(maxi, total)
print(maxi)

# kadane algo

n = len(nums)
maxi = float("-inf")
total = 0
for i in range(0, n):
    total = total + nums[i]
    maxi = max(maxi, total)
    if total < 0:
        total = 0
print(maxi)