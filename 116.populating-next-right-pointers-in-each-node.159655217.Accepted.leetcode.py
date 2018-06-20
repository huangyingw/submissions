class Solution:
    def connect(self, root):
        if not root:
            return

        if root.left:
            root.left.next = root.right

        if root.right:
            root.right.next = root.next.left if root.next else None

        self.connect(root.left)
        self.connect(root.right)
