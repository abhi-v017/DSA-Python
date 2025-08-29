nums = [0,1,2,4,5,6,7,8]
n = len(nums)

def missing_num(nums):
    for i in range(0, n):
        if i not in nums:
            return i
        
def missing_num2(nums):
    freq = {}
    for i in range(0, n+1):
        freq[i] = 0
    for nums in nums:
        freq[nums] = 1
    for k,v in freq.items():
        if v==0:
            return k
            
        

print(missing_num(nums))
print(missing_num2(nums))