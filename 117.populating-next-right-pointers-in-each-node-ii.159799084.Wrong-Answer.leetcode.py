class Solution:
    def connect(self, root):
        nav = None

        while root:
            if root.left:
                if nav:
                    nav.next = root.left
                nav = root.left
                print('nav --> %s' % nav.val if nav else '')

            if root.right:
                if nav:
                    nav.next = root.right
                nav = root.right
                print('nav --> %s' % nav.val if nav else '')
            root = root.next
            print('root --> %s' % root.val if root else '')
