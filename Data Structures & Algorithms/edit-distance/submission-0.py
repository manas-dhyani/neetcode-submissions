class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        d = {}

        def helper(m,n):
            
            if m >= len(word1):
                return len(word2) - n
            if n>= len(word2):
                return len(word1) - m
            
            if (m,n) in d:
                return d[(m,n)]
            
            if word1[m] == word2[n]:
                pick = helper(m+1,n+1)
                d[(m,n)] = pick
            else:
                ins = 1+ helper(m, n+1)
                dl = 1+ helper(m+1,n)
                rp = 1+helper(m+1,n+1)

                d[(m,n)] = min(ins, dl,rp)

            return d[(m,n)]

        return helper(0,0)