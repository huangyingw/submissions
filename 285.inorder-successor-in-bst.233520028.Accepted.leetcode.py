class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution(object):
    def inorderSuccessor(self, root, p):
        succ = None
        while root:
            if p.val >= root.val:
                root = root.right
            else:
                succ = root
                root = root.left
        return succ
class Solution2(object):
    def inorderSuccessor(self, root, p):
        if not root:
            return None
        if p.val >= root.val:
            return self.inorderSuccessor(root.right, p)
        left_succ = self.inorderSuccessor(root.left, p)
        return root if not left_succ else left_succ
