from collections import defaultdict, deque
def findOrder(self, V, prerequisites):
    adj = defaultdict(list)

    for u, v in prerequisites:
        adj[v].append(u)
    
    indegree = [0] * V
    for u in adj:
        for v in adj[u]:
            indegree[v] += 1

    q=deque()
    for i in range(V):
        if indegree[i]==0:
            q.append(i)
    topo=[]

    while q:
        node=q.popleft()
        topo.append(node)

        for n in adj[node]:
            indegree[n]-=1
            if indegree[n]==0:
                q.append(n)
    if len(topo)==V:
        return topo
    else:
        return []



            


    
    
    

    