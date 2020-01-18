class Solution(object):
    def searchBST(self, root, val):
        if not root:
            return None
        if root.val == val:
            return root
        elif root.val > val:
            root = root.left
        else:
            root = root.right
        return self.searchBST(root, val)
