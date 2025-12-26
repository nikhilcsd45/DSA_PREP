def climbStairs(self, n):
        dp=[-1]*(n+1)
        if n==1:
            return 1

        def f(n):
            if n==1 or n==0 :
                return 1
            if dp[n]!=-1:
                return dp[n]
            
            dp[n]=f(n-1)+f(n-2)
            return dp[n]

        f(n)
        return dp[n]

            
