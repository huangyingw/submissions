class Solution(object):
    def isSymmetric(self, root):
        if not root:
            return True
        return self.isMirror(root, root)
    def isMirror(self, l, r):
        if not l and not r:
            return True
        if not l or not r:
            return False
        if l.val == r.val:
            return self.isMirror(l.left, r.right) and self.isMirror(l.right, r.left)
        return False
