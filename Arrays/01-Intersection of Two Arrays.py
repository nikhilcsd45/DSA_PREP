def intersection(self, nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    set1=set(nums2)

    res=[]
    for i in nums1:
        if i in set1 :
            res.append(i)
    # for i in nums2:
    #     if i in nums1 and i in  nums2:
    #         set3.add(i)

    return list(set(res))