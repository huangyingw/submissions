class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def rightSideView(self, root):
        if not root:
            return []
        right_view = []
        layer = [root]
        while layer:
            right_view.append(layer[-1].val)
            next_layer = []
            for node in layer:
                if node.left:
                    next_layer.append(node.left)
                if node.right:
                    next_layer.append(node.right)
            layer = next_layer
        return right_view


class Solution2(object):
    def rightSideView(self, root):
        right_side = []
        self.recursive(root, 0, right_side)
        return right_side

    def recursive(self, node, depth, right_side):
        if not node:
            return
        if depth >= len(right_side):
            right_side.append(node.val)
        else:
            right_side[depth] = node.val
        self.recursive(node.left, depth + 1, right_side)
        self.recursive(node.right, depth + 1, right_side)
