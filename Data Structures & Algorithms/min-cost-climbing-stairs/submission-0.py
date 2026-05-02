#question on pick and not pick
class Solution:
    
    def helper(self,memo,n,cost):
        if n == 0 or n == 1:
            return cost[n]
        if n in memo:
            return memo[n]
        memo[n] = cost[n]+min(self.helper(memo, n-1,cost), self.helper(memo, n-2,cost))
        return memo[n]

        
        
        
    
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        l = len(cost)
        memo={}
        # if l == 1:
        #     return cost[n]
        memo[l-1] = min(self.helper(memo, l-1,cost),self.helper(memo, l-2,cost))
        return memo[l-1]