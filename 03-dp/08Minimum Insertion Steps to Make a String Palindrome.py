def minInsertions(self, s):
      s1=s
      s2=s[::-1]
      col=len(s2)
      row=len(s1)
      dp=[[0]*(col+1) for i in range(row+1)]
     
      for i in range(1,row+1):
        for j in range(1,col+1):
          if s1[i-1]==s2[j-1]:
            dp[i][j]=dp[i-1][j-1]+1
          else:
            dp[i][j]=max(dp[i][j-1],dp[i-1][j])
      res=dp[row][col]
      return col-res
       