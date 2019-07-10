








class Solution(object):
    def getMinimumDifference(self, root):

        self.min_diff = float("inf")
        self.prev = float("-inf")

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            self.min_diff = min(self.min_diff, node.val - self.prev)
            self.prev = node.val
            inorder(node.right)
        inorder(root)
        return self.min_diff
