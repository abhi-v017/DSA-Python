nums = [[1,2,3],[4,5,6],[7,8,9]]
row = len(nums)
col = len(nums[0])
for i in range(0, row):
    for j in range(0, col):
        print(nums[i][j], end=' ')
    print()

'''
# upper triangle
for i in range(0, row):
    for j in range(0, col):
        if j>=i:
            print(nums[i][j], end=' ')
        else:
            print('*', end=' ')
    print()
    
# lower triangle
for i in range(0, row):
    for j in range(0, col):
        if j<=i:
            print(nums[i][j], end=' ')
        else:
            print('*', end=' ')
    print()
'''
#transpose of matrix
result = [[0]*row for _ in range(col)]
for i in range(0, row):
    for j in range(0, col):
        result[j][i] = nums[i][j]
for i in range(0, row):
    for j in range(0, col):
        print(result[i][j], end=' ')
    print()