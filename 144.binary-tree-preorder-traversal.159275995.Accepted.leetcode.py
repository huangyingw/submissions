class Solution(object):
    def preorderTraversal(self, root):
        result = []

        def dfs(root):
            if not root:
                return
            result.append(root.val)
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return result
