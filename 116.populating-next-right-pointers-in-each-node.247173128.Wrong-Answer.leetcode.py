class Solution:
    def connect(self, root):
        current = [root] if root else []
        while current:
            nex = []
            prev = None
            for n in current:
                prev = n
                if n.left:
                    nex.append(n.left)
                if n.right:
                    nex.append(n.right)
            current = nex
        return root
