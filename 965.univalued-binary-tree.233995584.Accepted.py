_author_ = 'jake'
_project_ = 'leetcode'








class Solution:
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        value = root.val

        def helper(node):
            if not node:
                return True
            if node.val != value:
                return False
            return helper(node.left) and helper(node.right)
        return helper(root)
