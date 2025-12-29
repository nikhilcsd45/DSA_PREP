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
    


    
    
def deserialize(self, data):
    if not data:
        return []
    word=data.split(",")

    if word[0]=="null":
        return []
    
    q=deque()
    root=TreeNode(word[0])
    q.append(root)

    i=1
    l=len(data)
    while i<l and q:
        node=q.popleft()

        if i<l and word[i]!="null":
            node.left=TreeNode(int(word[i]))
            q.append(node.left)
        i+=1

        
        if i<l and word[i]!="null":
            node.right=TreeNode(int(word[i]))
            q.append(node.right)
        i+=1

    
    return root 
    