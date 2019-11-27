class Solution(object):
    def treeToDoublyList(self, root):
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
