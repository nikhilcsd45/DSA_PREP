from collections import defaultdict, deque
def amountOfTime(self, root, target):# target=start
        """
        :type root: Optional[TreeNode]
        :type start: int
        :rtype: int
        """ 
        if not root:
            return []

        adj=defaultdict(list)
        def build_graph(node,parent):
            if not node:
                return 
            if parent:
                adj[node.val].append(parent.val)
                adj[parent.val].append(node.val)

            build_graph(node.left,node)
            build_graph(node.right,node)
        build_graph(root,None)


        visited=set()
        q=deque()
        q.append(target)
        dis=0
        while q:
            l=len(q)


            for i in range(l):
                node=q.popleft()
                visited.add(node)
                for neigh in adj[node]:
                    if neigh not in visited:
                        q.append(neigh)
            dis+=1

        return dis-1
        


            
                    











        