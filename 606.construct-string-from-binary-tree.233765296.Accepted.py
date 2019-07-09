_author_ = 'jake'
_project_ = 'leetcode'

















class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        result = []

        def preorder(node):
            if not node:
                return
            result.append(str(node.val))
            if not node.left and not node.right:
                return
            result.append("(")
            preorder(node.left)
            result.append(")")
            if node.right:
                result.append("(")
                preorder(node.right)
                result.append(")")
        preorder(t)
        return "".join(result)
