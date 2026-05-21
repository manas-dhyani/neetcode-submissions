class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        diff = []
        n = len(gas)
        for i in range(len(gas)):
            diff.append(gas[i] - cost[i] )
        gs= 0 
        index = -1
        for i in range(n):

            gs=diff[i]
            if gs < 0:
                continue
  
            for j in range(i+1,n+i):  
                gs+= diff[j%n]
                if gs < 0:
                    break
            if gs >=0:
                index = i
                break
        return index 