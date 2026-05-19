class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        dp = {}

        def helper(i,prev):

            if i == len(nums):
                return 0
            
            if (i,prev) in dp:
                return dp[(i,prev)]
            
            if nums[i] >prev:
                pick = 1 + helper(i+1,nums[i])
                notpick = helper(i+1,prev)
                dp[(i,prev)] = max(pick, notpick)
                return dp[(i,prev)]
            else:
                dp[(i,prev)] = helper(i+1,prev)
                return dp[(i,prev)]

            
        return helper(0,-1001)
                
                



        