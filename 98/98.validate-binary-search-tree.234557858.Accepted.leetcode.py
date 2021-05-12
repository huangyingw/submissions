class Solution(object):
    def isValidBST(self, root, minn=float('-inf'), maxx=float('inf')):
        if not root:
            return True
        if root.val <= minn or root.val >= maxx:
            return False
        if not self.isValidBST(root.right, root.val, maxx):
            return False
        if not self.isValidBST(root.left, minn, root.val):
            return False
        return True
