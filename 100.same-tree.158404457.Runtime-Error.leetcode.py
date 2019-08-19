class Solution(object):
    def isSameTree(self, p, q):
        stackP = [p]
        stackQ = [q]
        while stackP and stackQ:
            p = stackP.pop()
            q = stackQ.pop()
            if p and q and p.val != p.val:
                return False
            stackP += [p.left]
            stackP += [p.right]
            stackQ += [q.left]
            stackQ += [q.right]
        return not stackP and not stackQ
