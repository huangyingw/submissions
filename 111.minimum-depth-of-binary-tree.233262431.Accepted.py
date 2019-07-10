class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def minDepth(self, root):
        if not root:
            return 0
        l = self.minDepth(root.left)
        r = self.minDepth(root.right)
        if not l or not r:
            return 1 + l + r
        return 1 + min(l, r)
