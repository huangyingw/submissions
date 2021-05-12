class Solution(object):
    def btreeGameWinningMove(self, root, n, x):
        self.left, self.right = 0, 0

        def count(node):
            if not node:
                return 0
            if node.val == x:
                self.left = count(node.left)
                self.right = count(node.right)
                return 0
            return 1 + count(node.left) + count(node.right)
        parent = count(root)
        results = sorted([parent, self.left, self.right])
        return results[-1] > sum(results[:2]) + 1
