class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def countUnivalSubtrees(self, root):
        self.univariates = 0
        self.is_univariate(root)
        return self.univariates

    def is_univariate(self, root):
        if not root:
            return True
        left_uni = self.is_univariate(root.left)
        right_uni = self.is_univariate(root.right)
        if left_uni and right_uni:
            if (not root.left or root.left.val == root.val) and (not root.right or root.right.val == root.val):
                self.univariates += 1
                return True
        return False


class Solution2(object):
    def countUnivalSubtrees(self, root):
        self.univariates = 0
        self.preorder(root)
        return self.univariates

    def preorder(self, root):
        if not root:
            return
        if self.is_univariate(root):
            self.univariates += 1
        self.preorder(root.left)
        self.preorder(root.right)

    def is_univariate(self, root):
        if not root:
            return True
        if root.left and root.left.val != root.val:
            return False
        if root.right and root.right.val != root.val:
            return False
        return self.is_univariate(root.left) and self.is_univariate(root.right)
