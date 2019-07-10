_author_ = 'jake'
_project_ = 'leetcode'














class Solution(object):
    def sufficientSubset(self, root, limit):

        if root.left is None and root.right is None:
            return None if root.val < limit else root
        if root.left:
            root.left = self.sufficientSubset(root.left, limit - root.val)
        if root.right:
            root.right = self.sufficientSubset(root.right, limit - root.val)
        return root if root.right or root.left else None
