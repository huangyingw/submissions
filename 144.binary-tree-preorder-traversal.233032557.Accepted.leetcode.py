class Solution(object):
    def preorderTraversal(self, root):
        if not root:
            return []
        stack, result = [root], []
        while stack:
            element = stack.pop()
            result.append(element.val)
            if element.right:
                stack.append(element.right)
            if element.left:
                stack.append(element.left)
        return result
class Solution(object):
    def preorderTraversal(self, root):
        result = []
        def recursive(root, result):
            if not root:
                return
            result.append(root.val)
            recursive(root.left, result)
            recursive(root.right, result)
        recursive(root, result)
        return result
