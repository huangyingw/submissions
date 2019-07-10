_author_ = 'jake'
_project_ = 'leetcode'









class Solution(object):
    def minDiffInBST(self, root):

        self.min_diff = float("inf")
        self.prev = float("-inf")

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            self.min_diff = min(self.min_diff, node.val - self.prev)
            self.prev = node.val
            inorder(node.right)
        inorder(root)
        return self.min_diff
