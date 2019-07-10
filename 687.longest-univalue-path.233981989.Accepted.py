_author_ = 'jake'
_project_ = 'leetcode'










class Solution(object):
    def longestUnivaluePath(self, root):

        self.longest = 0

        def helper(node):
            if not node:
                return 0, 0
            max_left = max(helper(node.left))
            max_right = max(helper(node.right))

            left = 1 + max_left if node.left and node.left.val == node.val else 0
            right = 1 + max_right if node.right and node.right.val == node.val else 0
            self.longest = max(self.longest, left + right)
            return left, right
        helper(root)
        return self.longest
