_author_ = 'jake'
_project_ = 'leetcode'










class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.helper(root, 0)

    def helper(self, node, partial):
        if not node:
            return 0
        partial = 10 * partial + node.val
        if not node.left and not node.right:
            return partial
        return self.helper(node.left, partial) + self.helper(node.right, partial)
