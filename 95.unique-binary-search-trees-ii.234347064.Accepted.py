class Solution:
    def generateTrees(self, n):
        if n == 0:
            return []
        return self.generateSubtree(1, n)

    def generateSubtree(self, start, end):
        if start > end:
            return [None]
        if start == end:
            return [TreeNode(start)]
        result = []
        for i in range(start, end + 1):
            leftsubtree = self.generateSubtree(start, i - 1)
            rightsubtree = self.generateSubtree(i + 1, end)
            for leftnode in leftsubtree:
                for rightnode in rightsubtree:
                    root = TreeNode(i)
                    root.left = leftnode
                    root.right = rightnode
                    result.append(root)
        return result
