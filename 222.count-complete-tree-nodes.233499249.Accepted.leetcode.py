class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution(object):
    def countNodes(self, root):
        if not root:
            return 0
        left_subtree = self.left_depth(root.left)
        right_subtree = self.left_depth(root.right)
        if left_subtree == right_subtree:
            return 2**left_subtree + self.countNodes(root.right)
        else:
            return 2**right_subtree + self.countNodes(root.left)
    def left_depth(self, node):
        depth = 0
        while node:
            node = node.left
            depth += 1
        return depth
