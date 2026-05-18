class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        '''
        q = deque
        curr cell =0
        res=1
        while q
        traverse for directions and check boundary condition
        append when new cell = 1
        new cell = 0 
        res +=1

        '''
        directions =[[1,0],[-1,0],[0,1],[0,-1]]
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0 

        def dfs(r,c):
            
            grid[r][c] =0
            area=0
            for dr, dc in directions:
                nr, nc = r + dr, c+ dc
                if nr>= 0 and nr<ROWS and nc>=0 and nc<COLS and grid[nr][nc] == 1:
                    area+=dfs(nr,nc)
            return 1 +area
            


        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    area = dfs(i,j)
                    islands = max(islands,area)
        return islands