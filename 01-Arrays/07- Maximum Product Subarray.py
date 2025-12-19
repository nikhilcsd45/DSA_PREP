def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        max_pro=nums[0]
        min_pro=nums[0]
        res=nums[0]

        for i in nums[1:]:
            if i <0:
                max_pro,min_pro=min_pro,max_pro
            
            max_pro=max(i,max_pro*i)
            min_pro=min(i,min_pro*i)

            res=max(res,max_pro)
        return res


        
            
        