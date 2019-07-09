_author_ = 'jake'
_project_ = 'leetcode'















class Solution(object):
    def checkEqualTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def make_sum(node):
            if not node:
                return 0
            node.val += make_sum(node.left) + make_sum(node.right)
            return node.val
        tree_sum = make_sum(root)
        if tree_sum % 2 == 1:
            return False

        def find_split(node):
            if not node:
                return False
            if node.left and node.left.val == tree_sum // 2:
                return True
            if node.right and node.right.val == tree_sum // 2:
                return True
            return find_split(node.left) or find_split(node.right)
        return find_split(root)
