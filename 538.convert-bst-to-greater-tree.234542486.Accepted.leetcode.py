class Solution(object):
    def convertBST(self, root):
        self.val = 0

        def visit(root):
            if root:
                visit(root.right)
                root.val += self.val
                self.val = root.val
                visit(root.left)
        visit(root)
        return root


class Solution(object):
    def convertBST(self, root):
        if not root:
            return None
        stack = [root]
        node = root.right
        sumVal = 0
        while stack or node:
            while node:
                stack.append(node)
                node = node.right
            node = stack.pop()
            sumVal += node.val
            node.val = sumVal
            node = node.left
        return root
