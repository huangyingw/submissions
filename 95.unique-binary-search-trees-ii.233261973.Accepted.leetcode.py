class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution(object):
    def generateTrees(self, n):
        if n <= 0:
            return []
        return self.generate(1, n)
    def generate(self, left, right):
        if left > right:
            return [None]
        results = []
        for i in range(left, right + 1):
            left_trees = self.generate(left, i - 1)
            right_trees = self.generate(i + 1, right)
            for l in left_trees:
                for r in right_trees:
                    root = TreeNode(i)
                    root.left = l
                    root.right = r
                    results.append(root)
        return results
