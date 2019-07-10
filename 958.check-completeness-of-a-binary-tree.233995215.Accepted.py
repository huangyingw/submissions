_author_ = 'jake'
_project_ = 'leetcode'









from collections import deque


class Solution:
    def isCompleteTree(self, root):

        queue = deque([root])
        while True:
            node = queue.popleft()
            if not node:
                return all(not nd for nd in queue)
            queue.append(node.left)
            queue.append(node.right)
