class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        d = {}
        def helper(i , buy):

            if i >= len(prices):
                return 0
            
            if (i,buy) in d:
                return d[(i,buy)]
            
            if buy:
                pick = -prices[i] + helper(i+1,0)
                notpick = helper(i+1,1)
                d[(i,buy)] = max(pick,notpick)
                return d[(i,buy)]
                
            else:
                pick = +prices[i] + helper(i+2,1)
                notpick = helper(i+1,0)
                d[(i,buy)] = max(pick,notpick)
                return d[(i,buy)]
        return helper(0,1)





