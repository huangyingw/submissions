class Solution(object):
    def isSameTree(self, p, q):
        stackP = [p]
        stackQ = [q]
        while stackP and stackQ:
            p = stackP.pop()
            q = stackQ.pop()

            if not p and not q:
                continue

            if not p or not q:
                return False

            if p and q and p.val != p.val:
                return False

            stackP.append(p.left)
            stackP.append(p.right)
            stackQ.append(q.left)
            stackQ.append(q.right)

        return not stackP and not stackQ
