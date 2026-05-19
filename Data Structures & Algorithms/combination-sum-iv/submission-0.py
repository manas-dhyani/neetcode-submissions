class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        dp = {}

        def helper(target):

            if target == 0:
                return 1

            if target < 0:
                return 0

            if target in dp:
                return dp[target]

            total = 0

            for n in nums:
                total += helper(target - n)

            dp[target] = total

            return total

        return helper(target)