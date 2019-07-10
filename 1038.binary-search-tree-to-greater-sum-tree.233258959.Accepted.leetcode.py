












class Solution(object):
    def bstToGst(self, root):

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
