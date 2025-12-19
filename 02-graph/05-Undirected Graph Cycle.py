from collections import defaultdict, deque
def isCycle(self, V, edge_list):
        # Build adjacency list from edge list
        edges = defaultdict(list)
        for u, v in edge_list:
            edges[u].append(v) 
            edges[v].append(u)
            
        visited = [0] * V
        
        def bfs(start):
            q = deque()
            q.append((start, -1))
            visited[start] = 1

            while q:
                node, parent = q.popleft()
                for neigh in edges[node]:
                    if visited[neigh] == 0:
                        visited[neigh] = 1
                        q.append((neigh, node))
                    elif neigh != parent:
                        return True
            return False

        for i in range(V):
            if visited[i] == 0:
                if bfs(i):
                    return True
        return False
