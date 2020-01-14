class Solution(object):
    def diameterOfBinaryTree(self, root):
        self.d = 1
        def depth(node):
            if not node:
                return 0
            l, r = depth(node.left), depth(node.right)
            self.d = max(self.d, l + r + 1)
            return max(l, r) + 1
        depth(root)
        return self.d - 1
