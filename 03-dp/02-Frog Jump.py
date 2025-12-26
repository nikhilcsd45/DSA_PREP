def minCost(self,arr):
    n=len(arr)
    dp=[0]*(n)
    dp[0]=0
    if n>1:
        dp[1]=abs(arr[1]-arr[0])
    
    for i in range(2,n):
        jump1=abs(arr[i]-arr[i-1])+dp[i-1]
        jump2=abs(arr[i]-arr[i-2])+dp[i-2]
        dp[i]=min(jump1,jump2)
    return dp[n-1]
        
        