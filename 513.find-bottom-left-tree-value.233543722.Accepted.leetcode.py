from collections import deque


class Solution(object):
    def findBottomLeftValue(self, root):
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)
        return node.val
