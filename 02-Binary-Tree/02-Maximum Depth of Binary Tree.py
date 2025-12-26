def maxDepth(self, root):
        
        def height(node):
            if not node:
                return 0
            
            lh=height(node.left)
            rh=height(node.right)
        
            return max(lh,rh)+1
        return height(root)