class Solution(object):
    def helper(self, left, right):
        if not left and not right:
            return True

        if not left or not right:
            return False

        return left.val == right.val and self.helper(left.left, right.right) and self.helper(left.right, right.left)

    def isSymmetric(self, root):
        if root:
            return self.helper(root.left, root.right)
        else:
            return None
