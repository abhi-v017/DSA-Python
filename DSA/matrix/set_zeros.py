nums = [[1,2,3],[4,0,6],[7,8,9]]
row = len(nums)
col = len(nums[0])
rowtrack = [0]*row
coltrack = [0]*col

for i in range(0, row):
    for j in range(0, col):
        if nums[i][j]==0:
            rowtrack[i] = -1
            coltrack[j] = -1
            
for i in range(0, row):
    for j in range(0, col):
        if rowtrack[i]==-1 or coltrack[j]==-1:
            nums[i][j] = 0
for i in range(0, row):
    for j in range(0, col):
        print(nums[i][j], end=' ')
    print()

#time complexity = O((n+m)+(n+m)+(n+m)) = O(3*(n+m)) = O(n+m)
#space complexity = O(n+m)