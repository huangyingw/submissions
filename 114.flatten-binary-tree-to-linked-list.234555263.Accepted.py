








class Solution(object):
    def flatten(self, root):

        node = root
        while node:
            if node.left:
                nodeL = node.left
                while nodeL.right:
                    nodeL = nodeL.right
                tmp, node.left = node.left, None
                nodeL.right, node.right = node.right, tmp
            node = node.right
