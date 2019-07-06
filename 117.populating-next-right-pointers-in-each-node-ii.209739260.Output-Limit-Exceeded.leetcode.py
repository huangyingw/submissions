class Solution:
    def connect(self, root):
        while root:
            leftMost = root.left
            while root:
                nav = leftMost
                if root.left and nav != root.left:
                    nav.next = root.left
                    nav = nav.next
                    if nav:
                if root.right and nav != root.right:
                    nav.next = root.right
                    nav = nav.next
                    if nav:
                if root.next:
                    root = root.next
                    if root:
            nav.next = None
            root = leftMost
            if root:
