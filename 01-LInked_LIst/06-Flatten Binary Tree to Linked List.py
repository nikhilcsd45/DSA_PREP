def flatten(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if root is None:
            return []
        
        st=[root]
        while st:
            node=st.pop()

            if node.right:
                st.append(node.right)
            if node.left:
                st.append(node.left)
            if st:
                node.right=st[-1]
                node.left=None
        return root