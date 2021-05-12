class Solution:
    def isBalanced(self, root):
        return self.checkBalance(root) != -1

    def checkBalance(self, root):
        if not root:
            return 0
        left = self.checkBalance(root.left)
        right = self.checkBalance(root.right)
        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1
        return max(left, right) + 1
