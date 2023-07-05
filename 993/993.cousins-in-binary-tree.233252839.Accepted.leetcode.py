class Solution(object):
    def adjacent(self, root, node1, node2):
        if not root:
            return False
        value = False
        if (root.right and root.left):
            value = ((root.left.val == node1 and root.right.val == node2) or
                     (root.left.val == node2 and root.right.val == node1))
        return (value or
                self.adjacent(root.left, node1, node2) or
                self.adjacent(root.right, node1, node2))

    def _level(self, root, node, level):
        if not root:
            return 0
        if root.val == node:
            return level
        left_level = self._level(root.left, node, level + 1)
        if left_level != 0:
            return left_level
        return self._level(root.right, node, level + 1)

    def isCousins(self, root, x, y):

        if ((self._level(root, x, 1) == self._level(root, y, 1)) and not self.adjacent(root, x, y)):
            return True
        return False
