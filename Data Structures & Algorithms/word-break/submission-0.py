class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        

        d = {}
        def helper(st,e):

            if (st,e) in d:
                return d[(st,e)]
            
            if e > len(s):
                return False

            if s[st:e] in wordDict:
                if e == len(s):
                    return True
                d[(st,e)] = helper(e,e+1) or helper(st,e+1)
                return d[(st,e)]
            else:
                d[(st,e)] = helper(st,e+1)
                return d[(st,e)]
        
        return helper(0,0)
        
            
            


            