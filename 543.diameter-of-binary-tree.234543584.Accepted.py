








class Solution:
    maxD = 0

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def maxDepth(root):
            """
            :type root: TreeNode
            :rtype: int
            """
            if root == None:
                return 0
            left = maxDepth(root.left)
            right = maxDepth(root.right)
            self.maxD = max(self.maxD, left + right)
            return max(left, right) + 1
        self.maxD = 0
        maxDepth(root)
        return self.maxD
