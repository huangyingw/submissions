_author_ = 'jake'
_project_ = 'leetcode'












class Solution(object):
    def sumRootToLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def helper(node, running):
            if not node:
                return 0
            running = running * 2 + node.val
            if not node.left and not node.right:
                return running
            return helper(node.left, running) + helper(node.right, running)
        return helper(root, 0) % (10 ** 9 + 7)
