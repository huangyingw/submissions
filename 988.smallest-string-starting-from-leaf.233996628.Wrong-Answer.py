












class Solution(object):
    def smallestFromLeaf(self, root):

        def helper(node):
            if not node:
                return ""
            node_char = chr(node.val + ord("a"))
            left, right = helper(node.left), helper(node.right)
            if not left or not right:
                return left + right + node_char
            return left + node_char if left < right else right + node_char
        return helper(root)
