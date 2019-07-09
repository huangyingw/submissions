_author_ = 'jake'
_project_ = 'leetcode'













class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        self.i = 0

        def helper(max_value=float("inf")):
            if self.i >= len(preorder) or preorder[self.i] > max_value:
                return None
            root = TreeNode(preorder[self.i])
            self.i += 1
            root.left = helper(root.val)
            root.right = helper(max_value)
            return root
        return helper()
