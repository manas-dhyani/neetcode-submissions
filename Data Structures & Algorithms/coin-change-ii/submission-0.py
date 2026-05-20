class Solution:
    def change(self, target: int, nums: List[int]) -> int:
        d = {} 
        def helper(i, target): 
            if target == 0:
                return 1 
            if i == len(nums) or target < 0:
                return 0
            if (i,target) in d: 
                return d[(i,target)] 
            d[(i,target)] = helper(i, target- nums[i]) + helper(i+1, target) 
            return d[(i,target)]
        return helper(0, target)