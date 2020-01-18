class Solution:
    def flatten(self, root):
        while root:
            if not root.right:
                root.left, root.right = root.right, root.left
            elif root.left:
                root.left, root.right = root.right, root.left
                it = root
                while it.right:
                    it = it.right
                root.left, it.right = it.right, root.left
            root = root.right
