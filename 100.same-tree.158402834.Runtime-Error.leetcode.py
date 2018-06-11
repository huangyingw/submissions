class Solution(object):
    def isSameTree(self, p, q):
        if not p or not q:
            return p == q

        if p.val == q.val:
            return True

        return isSameTree(self, p.left, q.left) and isSameTree(self, p.right, q.right)
