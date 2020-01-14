class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution(object):
    def preorderTraversal(self, root):
        if not root:
            return []
        preorder = []
        stack = [root]
        while stack:
            node = stack.pop()
            preorder.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return preorder
class Solution2(object):
    def preorderTraversal(self, root):
        result = []
        self.preorder(root, result)
        return result
    def preorder(self, node, result):
        if not node:
            return
        result.append(node.val)
        self.preorder(node.left, result)
        self.preorder(node.right, result)
