class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        visr=set()
        visc=set()

        def ro(r):
            for i in range(len(matrix[0])):
                matrix[r][i] = 0
        
        def co(c):
            for j in range(len(matrix)):
                matrix[j][c] = 0
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    visr.add(i)
                    visc.add(j)
        
        for r in visr:
            ro(r)
        for c in visc:
            co(c)



                     


