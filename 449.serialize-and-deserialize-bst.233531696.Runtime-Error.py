_author_ = 'jake'
_project_ = 'leetcode'












class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
from collections import deque


def serialize(self, root):

    serial_list = []

    def serial(node):
        if not node:
            return
        serial_list.append(str(node.val))
        serial(node.left)
        serial(node.right)
    serial(root)
    return " ".join(serial_list)


def deserialize(self, data):

    preorder = deque(int(val) for val in data.split())


    def deserial(low, high):
        if preorder and low < preorder[0] < high:
            val = preorder.popleft()
            node = TreeNode(val)
            node.left = deserial(low, val)
            node.right = deserial(val, high)
            return node
    return deserial(float("-inf"), float("inf"))
