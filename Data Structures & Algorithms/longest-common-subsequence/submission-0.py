class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        d = {}

        def helper(m,n):
            
            if m >= len(text1)  or n>= len(text2):
                return 0
            
            if (m,n) in d:
                return d[(m,n)]
            
            pick = 0 
            notpick = 0
            if text1[m] == text2[n]:
                pick = 1 + helper(m+1,n+1)
            
            notpick = max(helper(m+1, n), helper(m,n+1))

            d[(m,n)] = max(pick, notpick)

            return d[(m,n)]

        return helper(0,0)



            
            

            

            

        