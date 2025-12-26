from collections import deque
def shortestPathBinaryMatrix(self, grid):
        n = len(grid)
        m = len(grid[0])

        if grid[0][0] != 0 or grid[n-1][m-1] != 0:
            return -1
        
        dist = [[float('inf')] * m for _ in range(n)]
        dist[0][0] = 1 

        q = deque()
        q.append((1, 0, 0))  # (distance, row, col)

        # 8 directions: up, down, left, right, and diagonals
        dr = [-1, -1, -1, 0, 0, 1, 1, 1]
        dc = [-1, 0, 1, -1, 1, -1, 0, 1]

        while q:
            dis, r, c = q.popleft()

            if r == n - 1 and c == m - 1:
                return dis

            for i in range(8):
                newr = r + dr[i]
                newc = c + dc[i]

                if 0 <= newr < n and 0 <= newc < m and grid[newr][newc] == 0 and 1 + dis < dist[newr][newc]:
                    dist[newr][newc] = 1 + dis
                    q.append((1 + dis, newr, newc))

        return -1
