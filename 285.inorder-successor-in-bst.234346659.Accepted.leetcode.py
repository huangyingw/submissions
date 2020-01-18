class Solution(object):
    def inorderSuccessor(self, root, p):
        successor = None
        while root:
            if p.val < root.val:
                successor = root
                root = root.left
            else:
                root = root.right
        return successor

    def inorderSuccessor2(self, root, p):
        if not root:
            return None
        if p.val >= root.val:
            return self.inorderSuccessor(root.right, p)
        else:
            left = self.inorderSuccessor(root.left, p)
            return root if not left else left
