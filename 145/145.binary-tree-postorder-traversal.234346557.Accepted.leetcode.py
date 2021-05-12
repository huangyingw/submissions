class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def postorderTraversal(self, root):
        if root:
            return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]
        return []
