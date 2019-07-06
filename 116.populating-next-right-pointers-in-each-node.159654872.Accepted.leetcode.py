class Solution:
    def connect(self, root):
        if not root:
            return
        son = root.left
        while son:
            bak = root
            while son:
                son.next = root.right
                son = son.next
                root = root.next
                son.next = root.left if root else None
                son = son.next
            root = bak.left
            son = root.left
