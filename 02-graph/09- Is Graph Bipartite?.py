def dfs(self, node, col, color, adj):
        color[node] = col
        for neighbor in adj[node]:
            if color[neighbor] == -1:
                if not self.dfs(neighbor, 1 - col, color, adj):
                    return False
            elif color[neighbor] == col:
                return False

        return True

    
def isBipartite(self,adj):
    v=len(adj)
    color = [-1] * v

    for i in range(v):
        if color[i] == -1:
            if not self.dfs(i, 0, color, adj):
                return False

    return True
