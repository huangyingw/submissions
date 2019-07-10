_author_ = 'jake'
_project_ = 'leetcode'














class Solution(object):
    def maxDepth(self, root):

        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
