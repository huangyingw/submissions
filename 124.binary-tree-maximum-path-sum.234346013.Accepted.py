







class Solution:
    def maxPathSum(self, root):

        self.res = root.val
        self.dfs(root)
        return self.res

    def dfs(self, node):
        if not node:
            return 0
        left = max(0, self.dfs(node.left))
        right = max(0, self.dfs(node.right))
        self.res = max(self.res, left + right + node.val)
        return max(left, right) + node.val
