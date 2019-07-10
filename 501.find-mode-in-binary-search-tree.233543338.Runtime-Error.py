












class Solution(object):
    def findMode(self, root):

        self.prev = float("inf")
        self.count = 0
        self.mode_count = 0
        modes = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            if node.val == self.prev:
                self.count += 1
            else:
                self.prev = node.val
                self.count = 1
            if self.count == self.mode_count:
                modes.append(node.val)
            elif self.count > self.mode_count:
                self.mode_count = self.count
                modes.clear()
                modes.append(node.val)
            inorder(node.right)
        inorder(root)
        return modes
