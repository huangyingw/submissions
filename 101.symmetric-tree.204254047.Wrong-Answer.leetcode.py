class Solution(object):
    def dfs(self, left, right):
        if not left and not right:
            return True

        if not left or not right:
            return False

        return left.val == right.val and self.dfs(left.left, right.right) and self.dfs(left.right, right.left)

    def isSymmetric(self, root):
        if root:
            return self.dfs(root.left, root.right)
        else:
            return None
