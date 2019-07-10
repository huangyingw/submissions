








class Solution(object):
    def isUnivalTree(self, root):

        if not root:
            return True
        q = [root]
        val = root.val
        while q:
            temp = q.pop(0)
            if temp.val != val:
                return False
            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)
        return True
