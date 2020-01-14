class Solution:
    def sumNumbers(self, root):
        return self.getSum(root, 0)
    def getSum(self, node, s):
        if not node:
            return 0
        if not node.left and not node.right:
            return s * 10 + node.val
        return self.getSum(node.left, s * 10 + node.val) + self.getSum(node.right, s * 10 + node.val)
