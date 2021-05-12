import sys


class Solution(object):
    def isValidBST(self, root):
        return self.isVaild_helper(root, -sys.maxint - 1, sys.maxint)

    def isVaild_helper(self, root, minVal, maxVal):
        if root is None:
            return True
        if root.val >= maxVal or root.val <= minVal:
            return False
        return self.isVaild_helper(root.left, minVal, root.val) and self.isVaild_helper(root.right, root.val, maxVal)
