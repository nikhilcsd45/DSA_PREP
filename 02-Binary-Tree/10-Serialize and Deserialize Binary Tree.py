from collections import deque
def serialize(self, root):
        q=deque()
        res=[]
        q.append(root)

        while q:
            node=q.popleft()

            if node:
                res.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                res.append("null")
        
        return ",".join(res)
    


        
        

        
        