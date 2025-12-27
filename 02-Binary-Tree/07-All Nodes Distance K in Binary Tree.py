from collections import defaultdict, deque
def distanceK(self, root, target, k):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type k: int
        :rtype: List[int]
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
        q.append(target.val)
        dis=0
        while q:
            l=len(q)
            if dis==k:
                return [i for i in q]

            for i in range(l):
                node=q.popleft()
                visited.add(node)
                for neigh in adj[node]:
                    if neigh not in visited:
                        q.append(neigh)
            dis+=1

        return []