class Solution(object):
    def levelOrder(self, root):
        if not root:
            return []
        result = []
        level = [root]
        while level:
            new_level = []
            for node in level:
                new_level += node.children
            result.append([node.val for node in level])
            level = new_level
        return result
