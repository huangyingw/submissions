class Solution(object):
    def pruneTree(self, root):
        def contains_one(node):
            if not node:
                return False
            left_one, right_one = contains_one(node.left), contains_one(node.right)
            if not left_one:
                node.left = None
            if not right_one:
                node.right = None
            return node.val == 1 or left_one or right_one
        return root if contains_one(root) else None
