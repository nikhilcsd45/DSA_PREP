
def merge(self, nums1, m, nums2, n):
    i=m+n-1
    m-=1
    n-=1

    while m>-1 and n>-1:
        if nums1[m]>nums2[n]:
            nums1[i]=nums1[m]
            m-=1
        else:
            nums1[i]=nums2[n]
            n-=1
        
        i-=1
    while n >= 0:
        nums1[i] = nums2[n]
        n -= 1
        i -= 1




