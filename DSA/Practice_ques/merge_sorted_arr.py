nums1 = [1,2,3,4,5,6,7]
nums2 = [4,5,6,7,8,9]

def merge_arr(nums1, nums2):
    result = []
    n, m = len(nums1), len(nums2)
    i, j = 0, 0
    while i<n and j<m:
        if nums1[i]<=nums2[j]:
            if len(result)==0 or result[-1]!=nums1[i]:
                result.append(nums1[i])
            i+=1
        else:
            if len(result)==0 or result[-1]!=nums2[j]:
                result.append(nums2[j])
            j+=1
    while i<n:
        if len(result)==0 or result[-1]!=nums1[i]:
            result.append(nums1[i])
        i+=1
    while j<m:
        if len(result)==0 or result[-1]!=nums2[j]:
            result.append(nums2[j])
        j+=1
    return result
        

print(merge_arr(nums1,nums2))