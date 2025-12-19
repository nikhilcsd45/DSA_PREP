from collections import deque
def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        queue = deque()
        rows = len(grid)
        cols = len(grid[0])
        nonrotten=0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))
                elif grid[i][j]==1:
                    nonrotten+=1

        
        directions=[(-1,0),(0,1),(1,0),(0,-1)]
        t=0

        while queue:
            r,c,t=queue.popleft()
            for dr,dc in directions:
                nrow=r+dr
                ncol=c+dc

                if (0<=nrow<rows) and 0<=ncol<cols and grid[nrow][ncol]==1:
                    grid[nrow][ncol]=2
                    nonrotten-=1
                    queue.append((nrow,ncol,t+1))
        
        
        return t if nonrotten==0 else -1


        