class Solution(object):
    def levelOrder(self, root):
        if root is None:
            return []
        current, res = [root], []
        while current:
            nex, temp = [], []
            for n in current:
                temp.append(n.val)
                if n.left:
                    nex.append(n.left)
                if n.right:
                    nex.append(n.right)
            current = nex
            res.append(temp)
        return res
