class Solution(object):
    def isSymmetric(self, root):
        if not root:
            return True
        lqueue = [root.left]
        rqueue = [root.right]
        while lqueue and rqueue:
            lroot = lqueue.pop()
            rroot = rqueue.pop()
            if lroot != rroot:
                return False
            if not lroot and not rroot:
                return True
            lqueue.append(lroot.left)
            lqueue.append(lroot.right)
            rqueue.append(rroot.right)
            rqueue.append(rroot.left)
        return lroot == rroot
