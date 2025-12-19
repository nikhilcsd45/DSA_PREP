def findCircleNum(self, adj):
    """
    :type isConnected: List[List[int]]
    :rtype: int
    """
    l=len(adj)
    visited=[0]*l
    def dfs(node):
        visited[node]=1

        for neigh in range(len(adj[0])):
            if visited[neigh]==0 and adj[node][neigh]==1:
                dfs(neigh)

    count=0
    for i in range(l):
        if visited[i]==0:
            dfs(i)
            count+=1
    return count
    

        