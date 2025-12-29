class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def findUPar(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.findUPar(self.parent[node])
        return self.parent[node]

    def unionBySize(self, u, v):
        up_u = self.findUPar(u)
        up_v = self.findUPar(v)
        if up_u == up_v:
            return
        if self.size[up_u] < self.size[up_v]:
            self.parent[up_u] = up_v
            self.size[up_v] += self.size[up_u]
        else:
            self.parent[up_v] = up_u
            self.size[up_u] += self.size[up_v]

class Solution:
    def largestIsland(self, grid):
        n = len(grid[0])
        ds = DisjointSet(n * n)

        # Step 1: Union all 1s
        for row in range(n):
            for col in range(n):
                if grid[row][col] == 0:
                    continue
                for dr, dc in [(-1,0), (0,-1), (1,0), (0,1)]:
                    newr, newc = row + dr, col + dc
                    if 0 <= newr < n and 0 <= newc < n and grid[newr][newc] == 1:
                        nodeNo = row * n + col
                        adjNodeNo = newr * n + newc
                        ds.unionBySize(nodeNo, adjNodeNo)

        # Step 2: Try flipping every 0 to 1 and calculate max connected component
        mx = 0
        for row in range(n):
            for col in range(n):
                if grid[row][col] == 1:
                    continue
                components = set()
                for dr, dc in [(-1,0), (0,-1), (1,0), (0,1)]:
                    newr, newc = row + dr, col + dc
                    if 0 <= newr < n and 0 <= newc < n and grid[newr][newc] == 1:
                        components.add(ds.findUPar(newr * n + newc))
                sizeTotal = sum(ds.size[parent] for parent in components)
                mx = max(mx, sizeTotal + 1)

        # Edge case: grid full of 1s
        for cellNo in range(n * n):
            mx = max(mx, ds.size[ds.findUPar(cellNo)])

        return mx
