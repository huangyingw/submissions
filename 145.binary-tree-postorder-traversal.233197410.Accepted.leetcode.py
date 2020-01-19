class Solution(object):
    def postorderTraversal(self, root):
        result = []

        def recursive(root, result):
            if not root:
                return
            recursive(root.left, result)
            recursive(root.right, result)
            result.append(root.val)
        recursive(root, result)
        return result


class Solution(object):
    def postorderTraversal(self, root):
        if not root:
            return []
        stack, result = [], []
        while True:
            while root:
                if root.right:
                    stack.append(root.right)
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.right and stack and stack[-1] == root.right:
                stack.pop()
                stack.append(root)
                root = root.right
            else:
                result.append(root.val)
                root = None
            if len(stack) <= 0:
                break
        return result
