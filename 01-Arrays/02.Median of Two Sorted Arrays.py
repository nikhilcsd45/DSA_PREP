def findMedianSortedArrays(self, nums1, nums2):
    n = len(nums1) + len(nums2)
    k = n // 2
    left = right = counter = 0
    min_val = prevmin = 0

    # Merge until we reach the median position
    while left < len(nums1) and right < len(nums2):
        prevmin = min_val
        if nums1[left] <= nums2[right]:
            min_val = nums1[left]
            left += 1
        else:
            min_val = nums2[right]
            right += 1
        counter += 1

        if counter == k + 1:
            if n % 2 != 0:
                return float(min_val)
            else:
                return (prevmin + min_val) / 2.0

    while left < len(nums1):
        prevmin = min_val
        min_val = nums1[left]
        left += 1
        counter += 1

        if counter == k + 1:
            if n % 2 != 0:
                return float(min_val)
            else:
                return (prevmin + min_val) / 2.0

                
    while right < len(nums2):
        prevmin = min_val
        min_val = nums2[right]
        right += 1
        counter += 1

        if counter == k + 1:
            if n % 2 != 0:
                return float(min_val)
            else:
                return (prevmin + min_val) / 2.0

    return 0.0