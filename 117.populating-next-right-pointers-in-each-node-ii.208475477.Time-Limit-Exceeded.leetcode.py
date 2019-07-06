class Solution:
    def connect(self, root):
        while root:
            leftMost = root.left
            while root:
                nav = leftMost
                if root.left:
                    nav.next = root.left
                    nav = nav.next
                if root.right:
                    nav.next = root.right
                    nav = nav.next
                if root.next:
                    root = root.next
            nav.next = None
            root = leftMost
