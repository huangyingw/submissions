class Solution(object):
    def isSymmetric(self, root):
        if not root:
            return True
        lqueue = [root.left]
        rqueue = [root.right]
        while lqueue and rqueue:
            lroot = lqueue.pop()
            rroot = rqueue.pop()
            if not lroot and not rroot:
                continue
            if not lroot or not rroot:
                return False
            if lroot.val != rroot.val:
                return False
            lqueue += lroot.left
            lqueue += lroot.right
            rqueue += rroot.right
            rqueue += rroot.left
        return lroot == rroot
