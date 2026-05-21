class Solution:
    def isHappy(self, n: int) -> bool:
        vis = set()

        while n != 1:
            if n in vis:
                return False
            vis.add(n)
            sm = 0 
            while n != 0:
                rem = n%10
                sm += rem**2
                n = n//10
            n = sm 
        return True 

            
                        