def isMatch(self, s, p):
        dp=[[None]*len(p) for _ in range(len(s))]
        def f(i,j):
            if i < 0 and j < 0:
                return True
            elif j < 0:   
                return False
            elif i < 0:   
                for k in range(j, -1, -1):
                    if p[k] != '*':
                        return False
                return True
            if dp[i][j] is not None:
                return dp[i][j]

            if p[j] == '*':
                res=f(i - 1, j) or f(i, j - 1)

            elif p[j] == '?' or s[i] == p[j]:
                res= f(i - 1, j - 1)
            else:
                res=False
            
            dp[i][j]=res
            return res
            
        return f(len(s) - 1, len(p) - 1)
