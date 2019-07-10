










class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
from collections import deque


class Solution(object):
    def postorderTraversal(self, root):

        if not root:
            return []
        result = deque()
        stack = [root]
        while stack:
            node = stack.pop()
            result.appendleft(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return list(result)


class Solution2(object):
    def postorderTraversal(self, root):
        result = []
        self.postorder(root, result)
        return result

    def postorder(self, node, result):
        if not node:
            return
        self.postorder(node.left, result)
        self.postorder(node.right, result)
        result.append(node.val)
