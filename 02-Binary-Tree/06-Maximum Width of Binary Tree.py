from collections import deque

class Solution(object):
    def widthOfBinaryTree(self, root):
        if root is None:
            return 0


        queue = deque([(root, 0)])        #  (node, index)
        ans = 0

        while queue:
            size = len(queue)

        
            left_idx = queue[0][1]
            right_idx = queue[-1][1]

            ans = max(ans, right_idx - left_idx + 1)


            for _ in range(size):
                node, idx = queue.popleft()

                if node.left:
                    queue.append((node.left, 2 * idx + 1))
                if node.right:
                    queue.append((node.right, 2 * idx + 2))

        return ans
