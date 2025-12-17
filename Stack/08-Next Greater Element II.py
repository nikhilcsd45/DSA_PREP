def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans=[-1]*len(nums)
        st=[]
        l=len(nums)
        for i in range(2*l-1,-1,-1):
            ind=i%l
            while st and st[-1]<=nums[ind]:
                st.pop()
            if st and i<l:
                ans[i]=st[-1]
            st.append(nums[ind])
        return ans