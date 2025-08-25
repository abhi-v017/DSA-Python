def merge_sort(arr):
    if len(arr)<=1:
        return arr
    mid = len(arr)//2
    leftarr = arr[:mid]
    rightarr = arr[mid:]
    left = merge_sort(leftarr)
    right = merge_sort(rightarr)
    
    return merge_arr(left, right)

def merge_arr(left, right):
    result = []
    i,j = 0, 0
    n, m = len(left), len(right)
    while i<n and j<m:
        if left[i]<=right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    
    while i<n:
        result.append(left[i])
        i+=1
            
    while j<m:
        result.append(right[j])
        j+=1
    
    return result


nums = [1, 4, 6, 4, 8, 2, 0, 7, 5, 9]
print(merge_sort(nums))

# time complexity = O(nlogn)
# space complexity = O(1)