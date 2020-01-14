class FindElements(object):
    def __init__(self, root):
        self.elements = set()
        def helper(node, val):
            if not node:
                return
            self.elements.add(val)
            helper(node.left, 2 * val + 1)
            helper(node.right, 2 * val + 2)
        helper(root, 0)
    def find(self, target):
        return target in self.elements
