class Solution:
    def rob(self, nums):
        memo = {}

        def dfs(n, adj):
            if n == 0:
                return 0
            
            if (n, adj) in memo:
                return memo[(n, adj)]
            
            if adj:  # can pick
                pick = nums[n-1] + dfs(n-1, 0)
                notpick = dfs(n-1, 1)
                memo[(n, adj)] = max(pick, notpick)
            else:  # cannot pick
                memo[(n, adj)] = dfs(n-1, 1)
            
            return memo[(n, adj)]

        return dfs(len(nums), 1)