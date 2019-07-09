_author_ = 'jake'
_project_ = 'leetcode'













class Solution(object):
    def bstToGst(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.running = 0

        def inorder(node):
            if not node:
                return
            inorder(node.right)
            self.running += node.val
            node.val = self.running
            inorder(node.left)
        inorder(root)
        return root
