class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sm = 0 
        for i in range(len(nums)):
            sm+=nums[i]
        if sm%2!=0:
            return False
        sm = sm//2

        d = {}
        def helper(i, target):
            if target == 0:
                return True
            if i == len(nums):
                return False
            if (i,target) in d:
                return d[(i,target)]
            
            d[(i,target)] = helper(i+1, target- nums[i]) or helper(i+1, target)
            return d[(i,target)]
        return helper(0, sm)

        