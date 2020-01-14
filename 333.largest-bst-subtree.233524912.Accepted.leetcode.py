class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution(object):
    def largestBSTSubtree(self, root):
        self.largest = 0
        def is_bst(node):
            if not node:
                return float("-inf"), float("inf"), 0
            left_bst = is_bst(node.left)
            right_bst = is_bst(node.right)
            if left_bst[2] != -1 and right_bst[2] != -1:
                if left_bst[0] < node.val < right_bst[1]:
                    size = 1 + left_bst[2] + right_bst[2]
                    self.largest = max(self.largest, size)
                    return max(right_bst[0], node.val), min(left_bst[1], node.val), size
            return 0, 0, -1
        is_bst(root)
        return self.largest
