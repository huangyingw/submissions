class Solution(object):
    def inorderTraversal(self, root):
        res = []
        cur = root
        while cur != None:
            if cur.left == None:
                res.append(cur.val)
                cur = cur.right
            else:
                pre = cur.left
                while pre.right != None:
                    pre = pre.right
                pre.right = cur
                cur.left, cur = None, cur.left
        return res
