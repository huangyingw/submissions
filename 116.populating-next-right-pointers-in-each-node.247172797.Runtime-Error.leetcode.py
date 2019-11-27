class Solution:
    def connect(self, root):
        node = dummy = TreeLinkNode(0)
        while root:
            node.next = root.left
            if root.left:
                node = node.next
            node.next = root.right
            if root.right:
                node = node.next
            root = root.next
            if not root:
                node = dummy
                root = dummy.next
        return root
