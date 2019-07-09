_author_ = 'jake'
_project_ = 'leetcode'












class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.longest = 0

        def helper(node):
            if not node:
                return 0, 0
            l_i, l_d = helper(node.left)
            r_i, r_d = helper(node.right)
            incr, decr = 1, 1
            if node.left:
                if node.left.val == node.val + 1:
                    incr = 1 + l_i
                elif node.left.val == node.val - 1:
                    decr = 1 + l_d
            if node.right:
                if node.right.val == node.val + 1:
                    incr = max(incr, 1 + r_i)
                elif node.right.val == node.val - 1:
                    decr = max(decr, 1 + r_d)
            self.longest = max(self.longest, incr + decr - 1)
            return incr, decr
        helper(root)
        return self.longest
