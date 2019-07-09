_author_ = 'jake'
_project_ = 'leetcode'











class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def balanced(node):
            if not node:
                return 0
            left_depth = balanced(node.left)
            right_depth = balanced(node.right)
            if left_depth == -1 or right_depth == -1:
                return -1
            if abs(left_depth - right_depth) > 1:
                return -1
            return 1 + max(left_depth, right_depth)
        return balanced(root) != -1
