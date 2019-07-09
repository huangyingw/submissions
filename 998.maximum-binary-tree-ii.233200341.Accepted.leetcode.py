# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def insertIntoMaxTree(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        new_node = TreeNode(val)
        if not root:
            return new_node
        if root.val < val:
            new_node.left = root
            return new_node
        nrwwt = root
        start, prev = root.right, root
        while start:
            if(start.val > val):
                prev = start
                start = start.right
            else:
                break
        prev.right = new_node
        if not start:
            new_node.right = start
        else:
            new_node.left = start
        return root
