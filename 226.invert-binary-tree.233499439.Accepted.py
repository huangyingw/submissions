_author_ = 'jake'
_project_ = 'leetcode'







class Solution(object):
    def invertTree(self, root):

        if not root:
            return None
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root
