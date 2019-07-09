_author_ = 'jake'
_project_ = 'leetcode'









class TreeLinkNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        if not root:
            return
        level = [root]
        while level:
            next_level = []
            prev = None
            for node in level:
                if prev:
                    prev.next = node
                prev = node
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            level = next_level
