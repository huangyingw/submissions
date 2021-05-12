class Solution(object):
    def diameterOfBinaryTree(self, root):
        self.result = 0

        def helper(node):
            if not node:
                return -1
            left = helper(node.left)
            right = helper(node.right)
            self.result = max(self.result, 2 + left + right)
            return max(1 + left, 1 + right)
        helper(root)
        return self.result
