def canPartition(self, nums):

        target=sum(nums)
        if target%2!=0:
            return False
        target=target//2
        l=len(nums)
        dp=[[False]*(target+1) for _ in range(l+1)]

        for i in range(l+1):
            dp[i][0]=True
        for i in range(1,l+1):
            val=nums[i-1]
            for j in range(1,target+1):
                dp[i][j]=dp[i-1][j]

                if val<=j:
                    dp[i][j]=dp[i][j] or dp[i-1][j-val]
        return dp[l][target]
                    

        