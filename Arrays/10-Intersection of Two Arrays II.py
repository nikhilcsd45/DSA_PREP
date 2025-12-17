def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        dic={}
        for i in nums2:
            if i not in dic:
                dic[i]=0
            dic[i]+=1
        
        res=[]
        for i in nums1:
            if i in dic:
                res.append(i)
                dic[i]-=1
                if dic[i]==0:
                    del dic[i]   
        return res

