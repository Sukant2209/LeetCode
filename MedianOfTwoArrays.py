nums1 = [1,2]
nums2 = [3,4]

def median(nums1,nums2):
    med = 0

    l1 = len(nums1)
    l2=len(nums2)
    
    nums3 = nums1 + nums2

    nums3.sort()

    l3 = len(nums3)
    if l3 % 2 ==0:
            mid = l3//2
            med = (nums3[mid-1]+nums3[mid])/2
    else:
            mid = l3//2
            med = nums3[mid]

    return med


print(median(nums1,nums2))