class Solution(object):
    def dfs(self, root, result):
        if not root:
            return

        self.dfs(root.left, result)
        self.dfs(root.right, result)
        result.add(root.val)

    def postorderTraversal(self, root):
        result = []
        self.dfs(root, result)
        return result
