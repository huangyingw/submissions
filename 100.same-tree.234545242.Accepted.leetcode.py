class Solution:
    def isSameTree(self, p, q):
        def traverse(root):
            queue = [root]
            res = []
            while queue:
                temp = queue.pop(0)
                if temp:
                    res.append(temp.val)
                    queue.append(temp.left)
                    queue.append(temp.right)
                else:
                    res.append(None)
            return res
        lista = traverse(p)
        listb = traverse(q)
        return lista == listb
