_author_ = 'jake'
_project_ = 'leetcode'










class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def deleteNode(self, root, key):

        if not root:
            return None
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if not (root.left and root.right):
                root = root.left or root.right
            else:
                next_largest = root.right
                while next_largest.left:
                    next_largest = next_largest.left
                root.val = next_largest.val
                root.right = self.deleteNode(root.right, root.val)
        return root
