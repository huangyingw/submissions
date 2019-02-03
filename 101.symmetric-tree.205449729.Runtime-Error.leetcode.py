class Solution(object):
    def isSymmetric(self, root):
        lqueue = [root.left]
        rqueue = [root.right]

        while lqueue and rqueue:
            lroot = lqueue.pop()
            rroot = rqueue.pop()

            if lroot.val != rroot.val:
                return False

            lqueue.append(lroot.left)
            lqueue.append(lroot.right)
            rqueue.append(rroot.right)
            rqueue.append(rqueue.left)

        return lroot == rroot
