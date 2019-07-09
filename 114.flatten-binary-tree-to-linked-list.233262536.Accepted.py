_author_ = 'jake'
_project_ = 'leetcode'











class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        self.prev = None

    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        self.prev = root
        self.flatten(root.left)
        temp = root.right
        root.right = root.left
        root.left = None
        self.prev.right = temp
        self.flatten(temp)
