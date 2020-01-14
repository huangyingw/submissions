class Solution(object):
    def inorderTraversal(self, root):
        stack, result = [], []
        while root:
            stack.append(root)
            root = root.left
        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.right:
                node = node.right
                while node:
                    stack.append(node)
                    node = node.left
        return result
