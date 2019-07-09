_author_ = 'jake'
_project_ = 'leetcode'












class Solution:
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        def helper(node):
            if not node:
                return 0
            if node.val > R:
                return helper(node.left)
            if node.val < L:
                return helper(node.right)
            return node.val + helper(node.left) + helper(node.right)
        return helper(root)
