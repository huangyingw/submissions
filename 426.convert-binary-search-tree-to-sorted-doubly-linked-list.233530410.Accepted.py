_author_ = 'jake'
_project_ = 'leetcode'












class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None
        left_head = self.treeToDoublyList(root.left)
        right_head = self.treeToDoublyList(root.right)
        if left_head:
            root.left = left_head.left
            left_head.left.right = root
        else:
            left_head = root
        if right_head:
            root.right = right_head
            right_tail = right_head.left
            right_head.left = root
        else:
            right_tail = root
        left_head.left = right_tail
        right_tail.right = left_head
        return left_head
