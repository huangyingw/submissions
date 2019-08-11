class Solution(object):
    def hasPathSum(self, root, sum):
        if not root or root.val > sum:
            return False
        if root.val == sum:
            return True
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)
