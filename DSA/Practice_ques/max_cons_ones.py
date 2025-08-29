nums = [1,1,0,1,1,1,0,0,1,1,1,1,0,0,0,1]

def consecutive_one(nums):
    max = 0
    count = 0
    for nums in nums:
        if nums == 1:
            count +=1
        else:
            if count>max:
                max = count
            count = 0
    return max(max, count)

print(consecutive_one(nums))

# time complexity = O(n)
# space complexity = O(1)