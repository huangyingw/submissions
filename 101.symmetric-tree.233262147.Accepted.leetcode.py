class Solution(object):
    def isSymmetric(self, root):
        if not root:
            return True
        return self.is_mirror(root.left, root.right)

    def is_mirror(self, left_node, right_node):

        if not left_node and not right_node:
            return True

        if not left_node or not right_node:
            return False

        if left_node.val != right_node.val:
            return False

        return self.is_mirror(right_node.right, left_node.left) and \
            self.is_mirror(left_node.right, right_node.left)
