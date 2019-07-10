class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return sys.maxint
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        return min(left, right) + 1
