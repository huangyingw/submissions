class Solution(object):
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        traversal = []
        level = [root]
        forward = True
        while level:
            new_level = []
            if forward:
                traversal.append([n.val for n in level])
            else:
                traversal.append([n.val for n in level[::-1]])
            for node in level:
                if node.left:
                    new_level.append(node.left)
                if node.right:
                    new_level.append(node.right)
            level = new_level
            forward = not forward
        return traversal
