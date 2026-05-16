class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp ={}
        def helper(i,amount):
            if (i, amount) in dp:
                return dp[(i, amount)]
            if amount == 0:
                return 0
            if i == len(coins) or amount<0:

                return math.inf

            pick = 1 + helper(i,amount-coins[i]) 

            notpick = helper(i+1, amount)

            dp[(i, amount)] = min(pick,notpick)
            
            return dp[(i, amount)]
        x = helper(0,amount)
        if x == math.inf:
            return -1
        return x

