def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ans=[-1]*len(nums2)
        st=[]
        l=len(nums2)
        for i in range(l-1,-1,-1):
            while st and st[-1]<nums2[i]:
                st.pop()
            if st:
                ans[i]=st[-1]
            st.append(nums2[i])
        
        res=[]
        for i in nums1:
            ind=nums2.index(i)
            res.append(ans[ind])
        return res
        