class Solution(object):
    def __init__(self):
        self.result = []

    def dfs(self, root, current):
        if not root:
            return
        if not root.left and not root.right:
            self.result.append(current + root.val)
        self.dfs(root.left, current + str(root.val) + '->')
        self.dfs(root.right, current + str(root.val) + '->')

    def binaryTreePaths(self, root):
        self.dfs(root, '')
        return self.result
