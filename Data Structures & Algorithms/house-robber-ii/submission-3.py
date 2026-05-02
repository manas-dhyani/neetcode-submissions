class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        memo = {}
        memo2 ={}

        def dfs(n, adj,nums,memo):
            if n == 0:
                return 0
            
            if (n, adj) in memo:
                return memo[(n, adj)]
            
            if adj:  # can pick
                pick = nums[n-1] + dfs(n-1, 0,nums,memo)
                notpick = dfs(n-1, 1,nums,memo)
                memo[(n, adj)] = max(pick, notpick)
            else:  # cannot pick
                memo[(n, adj)] = dfs(n-1, 1,nums,memo)
            
            return memo[(n, adj)]

        return max(dfs(len(nums[1:]), 1,nums[1:],memo),dfs(len(nums[:len(nums)-1]), 1,nums[:len(nums)-1],memo2)) 
        