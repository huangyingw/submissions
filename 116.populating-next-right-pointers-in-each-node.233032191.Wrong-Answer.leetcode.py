# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None


class Solution:
    # @param root, a tree link node
    # @return nothing
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
