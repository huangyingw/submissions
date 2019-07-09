_author_ = 'jake'
_project_ = 'leetcode'








class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if not root:
            return 0
        if not root.children:
            return 1
        return 1 + max(self.maxDepth(child) for child in root.children)
