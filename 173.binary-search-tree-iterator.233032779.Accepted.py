'''
	Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.
	Calling next() will return the next smallest number in the BST.
	Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
'''


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
