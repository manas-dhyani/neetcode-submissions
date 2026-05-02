class Solution:
    
    def helper(self,memo,n)->int:
        
        if n==0 or n==1:
            return 1
        if n in memo:
            return memo[n]
        memo[n] = self.helper(memo,n-1) + self.helper(memo,n-2)
        return memo[n]
    def climbStairs(self, n: int) -> int:
        memo ={}
        if n == 1:
            return 1
        self.helper(memo,n)
        return memo[n]
        