# class Solution(object):
#     def longestCommonSubsequence(self, text1, text2):
#         n=len(text1)
#         m=len(text2)

#         dp=[[-1]*(m) for i in range(n)]

#         def f(i,j):
#             if i<0 or j <0:
#                 return 0
#             if dp[i][j]!=-1:
#                 return dp[i][j]

#             if text1[i]==text2[j]:
#                 return 1+ f(i-1,j-1)
#             else:
#                 dp[i][j]=max(f(i-1,j),f(i,j-1))
#             return dp[i][j]
            
#         return f(n-1,m-1)


            
        
# class Solution(object):
#     def longestCommonSubsequence(self, text1, text2):
#         n = len(text1)
#         m = len(text2)
        
#         # dp[i][j] = LCS length for text1[0..i-1], text2[0..j-1]
#         dp = [[0] * (m + 1) for _ in range(n + 1)]

#         # Build table
#         for i in range(1, n + 1):
#             for j in range(1, m + 1):
#                 if text1[i - 1] == text2[j - 1]:
#                     dp[i][j] = 1 + dp[i - 1][j - 1]
#                 else:
#                     dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
#         return dp[n][m]




class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        n = len(text1)
        m = len(text2)
        
        prev=[0]*(m+1)
        # Build table
        for i in range(1, n + 1):
            curr=[0]*(m+1)
            for j in range(1, m + 1):
                if text1[i - 1] == text2[j - 1]:
                    curr[j] = 1 + prev[j-1]
                else:
                    curr[j]=max(prev[j],curr[j-1])
            prev=curr
        return prev[m]



        
        