class Solution(object):
    def addOneRow(self, root, v, d):
        if not root:
            return None
        if d == 1:
            root, root.left = TreeNode(v), root
        elif d == 2:
            old_left, old_right = root.left, root.right
            root.left, root.right = TreeNode(v), TreeNode(v)
            root.left.left, root.right.right = old_left, old_right
        else:
            self.addOneRow(root.left, v, d - 1)
            self.addOneRow(root.right, v, d - 1)
        return root
