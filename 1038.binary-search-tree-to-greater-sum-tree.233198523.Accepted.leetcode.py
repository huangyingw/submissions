







class Solution(object):
    def bstToGst(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.curr_sum = 0

        def greaterSum(root):
            if not root:
                return
            greaterSum(root.right)
            self.curr_sum += root.val
            root.val = self.curr_sum
            greaterSum(root.left)
        greaterSum(root)
        return root
