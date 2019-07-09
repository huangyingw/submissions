_author_ = 'jake'
_project_ = 'leetcode'











class Solution(object):
    def maxAncestorDiff(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def helper(node, min_val, max_val):
            if not node:
                return max_val - min_val
            min_val = min(node.val, min_val)
            max_val = max(node.val, max_val)
            return max(helper(node.left, min_val, max_val), helper(node.right, min_val, max_val))
        return helper(root, float("inf"), float("-inf"))
