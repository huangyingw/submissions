class Solution(object):
    def boundaryOfBinaryTree(self, root):
        def left_side(node):
            if not node or (not node.left and not node.right):
                return
            boundary.append(node.val)
            if node.left:
                left_side(node.left)
            else:
                left_side(node.right)

        def right_side(node):
            if not node or (not node.left and not node.right):
                return
            right_edge.append(node.val)
            if node.right:
                right_side(node.right)
            else:
                right_side(node.left)

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            if not node.left and not node.right:
                boundary.append(node.val)
            inorder(node.right)
        if not root:
            return []
        boundary, right_edge = [root.val], []
        left_side(root.left)
        inorder(root.left)
        inorder(root.right)
        right_side(root.right)
        return boundary + right_edge[::-1]
