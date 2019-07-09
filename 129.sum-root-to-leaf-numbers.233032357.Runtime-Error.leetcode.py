# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        def dfs(root, num, total):
            if not root:
                return total
            num = num * 10 + root.val
            if not root.left and not root.right:
                total += num
                return total
            return dfs(root.left, num) + dfs(root.right, num)
        return dfs(root, 0, 0)
