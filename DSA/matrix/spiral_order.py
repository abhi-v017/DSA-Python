nums = [[1,2,3],[4,5,6],[7,8,9]]
n = len(nums)
row = len(nums)
col = len(nums[0])
left = 0
right = col-1
top = 0
bottom = row-1
result = []
while top<=bottom and left<=right:
    for i in range(left, right+1):
        result.append(nums[top][i])
    top+=1
    for i in range(top, bottom+1):
        result.append(nums[i][right])
    right-=1
    if top<=bottom:
        for i in range(right, left-1, -1):
            result.append(nums[bottom][i])
        bottom-=1
    if left<=right:
        for i in range(bottom, top-1, -1):
            result.append(nums[i][left])
        left+=1
for i in range(0, row):
    for j in range(0, col):
        print(nums[i][j], end=' ')
    print()
print(result)

#time complexity = O(n*m)
#space complexity = O(1)