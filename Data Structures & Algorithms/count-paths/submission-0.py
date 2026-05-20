class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        d ={}
        def helper(r,c):
            if r == m and c == n:
                return 1
            if r > m or c > n:
                return 0
            

            if (r,c) in d:
                return d[(r,c)]

            dw = helper(r+1,c)
            rt = helper(r,c+1)

            d[(r,c)] = dw+rt
            return d[(r,c)]
        return helper(1,1)
        
