class Solution(object):
    def __init__(self):
        self.first = self.second = None
        self.pre = TreeNode(-sys.maxint - 1)

    def recoverTree(self, root):
        self.traverse(root)
        self.first.val, self.second.val = self.second.val, self.first.val

    def traverse(self, root):
        if root is None:
            return
        self.traverse(root.left)
        if self.pre.val >= root.val:
            if self.first is None:
                self.first = self.pre
            if self.first is not None:
                self.second = root
        self.pre = root
        self.traverse(root.right)
