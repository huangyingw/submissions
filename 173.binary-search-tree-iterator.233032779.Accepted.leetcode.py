







class BSTIterator(object):
    def __init__(self, root):

        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    def hasNext(self):

        return self.stack

    def next(self):

        node = self.stack.pop()
        new_node = node.right
        while new_node:
            self.stack.append(new_node)
            new_node = new_node.left
        return node.val
