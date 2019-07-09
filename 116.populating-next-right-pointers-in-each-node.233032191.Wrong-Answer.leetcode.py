








class Solution:


    def connect(self, root):
        def recursive(node):
            if node is None:
                return
            if node.left:
                node.left.next = node.right
            if node.right:
                if node.next:
                    node.right.next = node.next.left
                else:
                    node.right.next = None
            recursive(node.left)
            recursive(node.right)
            if root != None:
                root.next = None
                recursive(root)
