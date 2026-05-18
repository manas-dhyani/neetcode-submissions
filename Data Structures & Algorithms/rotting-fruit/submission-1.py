class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visit = set()
        q = deque()
        
        def addCell(r,c):
            if min(r,c)<0 or r == ROWS or c  == COLS or (r,c) in visit or grid[r][c] == 0:
                return
            grid[r][c] = 2
            visit.add((r,c))
            q.append([r,c])


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append([r,c])
                    visit.add((r,c))
        time = -1
        while q:
            time+=1
            for i in range(len(q)):
                r,c = q.popleft()    
                addCell(r+1, c)
                addCell(r-1, c)
                addCell(r, c+1)
                addCell(r,c-1)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return -1
        return max(time,0)
    
        