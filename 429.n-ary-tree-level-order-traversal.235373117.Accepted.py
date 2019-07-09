_author_ = 'jake'
_project_ = 'leetcode'







class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
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
