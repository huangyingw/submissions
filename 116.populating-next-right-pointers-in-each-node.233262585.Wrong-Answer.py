class Solution(object):
    def connect(self, root):
        level = [root]
        while level and level[0]:
            next_level = []
            prev = None
            for node in level:
                if prev:
                    prev.next = node
                prev = node
                next_level.append(node.left)
                next_level.append(node.right)
            level = next_level
