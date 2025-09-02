# rotate matrix by 90 degree => formula => (n-1)-i
nums = [[1,2,3],[4,5,6],[7,8,9]]
n = len(nums)
row = len(nums)
col = len(nums[0])
result = [[0]*row for _ in range(col)]
for i in range(0, row):
    for j in range(0, col):
        result[j][(n-1)-i] = nums[i][j]
for i in range(0, row):
    for j in range(0, col):
        print(nums[i][j], end=' ')
    print()
rowr = len(nums)
colr = len(nums[0])
for i in range(0, rowr):
    for j in range(0, colr):
        print(result[i][j], end=' ')
    print()
    
#time complexity = O(n^2)
#space complexity = O(n^2)