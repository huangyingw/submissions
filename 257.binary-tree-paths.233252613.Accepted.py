







class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        paths = []

        def dfs(root, curr):
            if root.left is None and root.right is None:
                paths.append(curr + str(root.val))
                return
            if root.left:
                dfs(root.left, curr + str(root.val) + '->')
            if root.right:
                dfs(root.right, curr + str(root.val) + '->')
        curr = ""
        dfs(root, curr)
        return paths
