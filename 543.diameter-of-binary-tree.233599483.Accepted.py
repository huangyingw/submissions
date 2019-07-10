











class Solution(object):
    def diameterOfBinaryTree(self, root):

        if not root:
            return 0
        self.diameter = 0

        def helper(node):
            left_longest = 0 if not node.left else 1 + max(helper(node.left))
            right_longest = 0 if not node.right else 1 + max(helper(node.right))
            self.diameter = max(self.diameter, left_longest + right_longest)
            return (left_longest, right_longest)
        helper(root)
        return self.diameter
