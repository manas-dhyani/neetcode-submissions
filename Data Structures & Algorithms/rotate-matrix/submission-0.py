class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])
        for i in range(rows):
            for j in range(cols):
                if i != j and j>i:
                    matrix[i][j], matrix[j][i]=matrix[j][i], matrix[i][j]

        for i in range(rows):
            matrix[i] = matrix[i][::-1]
        
                    
        