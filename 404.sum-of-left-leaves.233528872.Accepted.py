_author_ = 'jake'
_project_ = 'leetcode'







class Solution(object):
    def sumOfLeftLeaves(self, root):

        if not root:
            return 0
        if root.left and not root.left.left and not root.left.right:
            return root.left.val + self.sumOfLeftLeaves(root.right)
        return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)
