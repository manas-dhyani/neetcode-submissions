class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        dp = {}

        def helper(i, target):

            if target == 0:
                return 1

            if i == len(coins) or target < 0:
                return 0

            if (i, target) in dp:
                return dp[(i, target)]

            take = helper(i, target - coins[i])

            skip = helper(i + 1, target)

            dp[(i, target)] = take + skip

            return dp[(i, target)]

        return helper(0, amount)