class Solution(object):
    def isSymmetric(self, left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        return left.val == right.val and self.isSymmetric(left.left, right.right) and self.isSymmetric(left.right, right.left)

    def isSymmetric(self, root):
        return self.isSymmetric(root.left, root.right)
