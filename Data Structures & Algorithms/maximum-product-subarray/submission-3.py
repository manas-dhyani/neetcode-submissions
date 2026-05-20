class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currMin = 1
        currMax =1
        res = max(nums)

        for n in nums:
            tmp = currMax * n
            currMax = max(n*currMax, n*currMin, n)
            currMin = min(n*currMin, tmp, n)

            res = max(currMax,res)

        return res            

