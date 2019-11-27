class Solution(object):
    def isSymmetric(self, root):
        return self.isMirror(root, root)

    def isMirror(self, node1, node2):
        if not node1 and not node2:
            return True
        elif not node1 or not node2:
            return False
        else:
            if node1.val == node2.val:
                return self.isMirror(node1.left, node2.right) and self.isMirror(node1.right, node2.left)
            else:
                return False
