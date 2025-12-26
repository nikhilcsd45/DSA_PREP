def postorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]

        """
        if not root:
            return []
        ans=[]
        st=[]
        st.append(root)
        while st:
            temp=st.pop()
            ans.append(temp.val)
            if temp.left:
                st.append(temp.left)
            if temp.right:
                st.append(temp.right)
        return ans[::-1]
                

    

        