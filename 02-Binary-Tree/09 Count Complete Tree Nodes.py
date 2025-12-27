def countNodes(self, root):
        if not root:
            return 0
        return 1 + self.sub_tree(root.left) + self.sub_tree(root.right)

def sub_tree(self, node):
        if not node:
            return 0
        lh = self.traversal_l(node)
        rh = self.traversal_r(node)
        if lh == rh:
            return (1 << lh) - 1  # complete subtree formula: 2^h - 1
        return self.countNodes(node)

def traversal_l(self, node):
        count = 0
        while node:
            count += 1
            node = node.left
        return count

def traversal_r(self, node):
        count = 0
        while node:
            count += 1
            node = node.right
        return count
