_author_ = 'jake'
_project_ = 'leetcode'










class Solution(object):
    def searchBST(self, root, val):

        if not root:
            return None
        if root.val == val:
            return root
        if val > root.val:
            return self.searchBST(root.right, val)
        return self.searchBST(root.left, val)
