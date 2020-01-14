class Solution(object):
    def longestUnivaluePath(self, root):
        self.longest = 0
        def traverse(node):
            if not node:
                return 0
            left_len, right_len = traverse(node.left), traverse(node.right)
            left = (left_len + 1) if node.left and node.left.val == node.val else 0
            right = (right_len + 1) if node.right and node.right.val == node.val else 0
            self.longest = max(self.longest, left + right)
            return max(left, right)
        traverse(root)
        return self.longest
