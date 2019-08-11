class Solution(object):
    def inorderTraversal(self, root):
        result = []
        stack = [root]
        while stack or root:
            if root.left:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                result.append(root.val)
                root = root.right
        return result
