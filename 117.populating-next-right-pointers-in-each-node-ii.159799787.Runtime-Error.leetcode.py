class Solution:
    def connect(self, root):
        nav = None
        leftMost = None
        while root:
            while root:
                if not leftMost:
                    leftMost = root.left if root.left else root.right
                if root.left:
                    if nav:
                        nav.next = root.left
                    nav = root.left
                if root.right:
                    if nav:
                        nav.next = root.right
                    nav = root.right
                root = root.next
            root = leftMost.left if leftMost.left else leftMost.right
