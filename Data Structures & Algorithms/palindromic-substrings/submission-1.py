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
        print(l)
        return left+1, right-1,l

    def countSubstrings(self, s: str) -> int:
        maxi = 0
        left=0
        right=0
        for i in range(0,len(s)):
            # if i == 0:
            #     maxi+=1
            #     continue
            
            left1, right1, even = self.ispalindrome(i,i+1,s)
            left2, right2, odd = self.ispalindrome(i,i,s)
            maxi += even + odd 
        return maxi
        
