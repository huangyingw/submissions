class Solution(object):
    def isBalanced(self, root):
        if root == None:
            return True
        flag = abs(self.maxDepth(root.left) - self.maxDepth(root.right)) <= 1
        return flag and self.isBalanced(root.left) and self.isBalanced(root.right)

    def maxDepth(self, root):
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

    def isBalanced(self, root):
        def dfs(root):
            if root is None:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            return max(left, right) + 1
        return dfs(root) != -1
