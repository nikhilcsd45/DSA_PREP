def binaryTreePaths(self, root):
        if not root:
            return []
        ans=[]

        def f(node,path):
            path.append(str(node.val))

            if not node.left and not node.right:
                ans.append("->".join(path))
                return 
            else:
                if node.left:
                    f(node.left,path)
                    path.pop()
                if node.right:
                    f(node.right,path)
                    path.pop()
        f(root,[])
        return ans
                
            


            