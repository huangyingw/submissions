_author_ = 'jake'
_project_ = 'leetcode'











class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    def hasNext(self):
        """
        :rtype: bool
        """
        return True if self.stack else False

    def next(self):
        """
        :rtype: int
        """
        node = self.stack.pop()
        result = node.val
        if node.right:
            node = node.right
            while node:
                self.stack.append(node)
                node = node.left
        return result
