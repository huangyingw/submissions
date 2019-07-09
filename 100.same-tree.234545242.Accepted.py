








class Solution:

    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False



    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
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
