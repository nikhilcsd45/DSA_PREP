
from collections import defaultdict
def getComponents(self, V, edges):
        
        adj=defaultdict(list)
        ans=[]
        visited=[0]*V
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        def dfs(node,path):
            visited[node]=1
            path.append(node)
            
            for neigh in adj[node]:
                if visited[neigh]==0:
                    dfs(neigh,path)
           
                
        for i in range(V):
            if visited[i]==0:
                path=[]
                dfs(i,path)
                ans.append(path)
        return ans
    