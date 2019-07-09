_author_ = 'jake'
_project_ = 'leetcode'








class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return []
        stack = [root]
        result = []
        while stack:
            node = stack.pop()
            result.append(node.val)
            for child in reversed(node.children):
                stack.append(child)
        return result
