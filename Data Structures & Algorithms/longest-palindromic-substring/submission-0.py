class Solution:
    def ispalindrome(self,left,right,s):
        l=0
        while(left>=0 and right<len(s)):
            if s[left] == s[right]:
                l+=1
                left-=1
                right+=1
                continue
            break
        return left+1, right-1,right -left

    def longestPalindrome(self, s: str) -> str:
        maxi = 1
        left=0
        right=0
        for i in range(0,len(s)-1):
            left1, right1, even = self.ispalindrome(i,i+1,s)
            left2, right2, odd = self.ispalindrome(i,i,s)
            if maxi < even:
                left = left1
                right = right1
                maxi = even
            if maxi < odd:
                left = left2
                right = right2
                maxi = odd
        return s[left:right+1]