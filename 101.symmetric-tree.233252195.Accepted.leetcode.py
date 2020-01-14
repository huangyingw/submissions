class Solution(object):
    def isSymmetric(self, root):
        if not root:
            return True
        def dfs(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            return (left.val == right.val) and dfs(left.left, right.right) and dfs(left.right, right.left)
        return dfs(root, root)
