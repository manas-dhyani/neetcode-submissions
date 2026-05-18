class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # we check boundary for rows and col and check not equal 0
        # dierction 2 d list
        #grid[curr] = 0
        # for dr dc in direction
        # 2 d traverse chec
        # grid[row][col] == 1 traverse using dfs then island ++

        directions =[[1,0],[-1,0],[0,1],[0,-1]]
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0 

        def dfs(r,c):

            grid[r][c] ="0"
            for dr, dc in directions:
                nr, nc = r + dr, c+ dc
                if nr>= 0 and nr<ROWS and nc>=0 and nc<COLS and grid[nr][nc] == "1":
                    dfs(nr,nc)


        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1":
                    dfs(i,j)
                    islands+=1
        return islands

        






































        
