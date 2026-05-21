class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}

        def helper(i, target):

            if target == 0 and i == len(nums):
                return 1

            if i == len(nums):
                return 0
            

            if (i, target) in dp:
                return dp[(i, target)]

            take = helper(i + 1, target - nums[i])
            take_min = helper(i+1,target +nums[i])

            dp[(i, target)] = take  + take_min

            return dp[(i, target)]

        return helper(0, target)
        