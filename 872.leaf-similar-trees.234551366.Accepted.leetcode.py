class Solution(object):
    def leafSimilar(self, root1, root2):
        return self.leafInorder(root1) == self.leafInorder(root2)
    def leafInorder(self, root):
        if not root:
            return []
        if not root.left and not root.right:
            return [root.val]
        return self.leafInorder(root.left) + self.leafInorder(root.right)
