class Solution:
    def maxDepth(self, root):
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
    def maxDepth(self, root):
        stack = [(root, 1)]
        total = 0
        while stack:
            node, depth = stack.pop()
            if node:
                total = max(total, depth)
                stack.extend([(node.left, depth + 1), (node.right, depth + 1)])
        return total
