class Solution(object):
    def inorderTraversal(self, root):
        result = []
        stack = [root]
        while stack:
            if root.left:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                result.append(root)
                root = root.right
        return result
