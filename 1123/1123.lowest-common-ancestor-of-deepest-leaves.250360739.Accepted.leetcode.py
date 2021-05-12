class Solution(object):
    def lcaDeepestLeaves(self, root):
        def helper(node):
            if not node:
                return None, 0
            left_lca, left_depth = helper(node.left)
            right_lca, right_depth = helper(node.right)
            if left_depth == right_depth:
                return node, left_depth + 1
            if left_depth > right_depth:
                return left_lca, left_depth + 1
            return right_lca, right_depth + 1
        result, _ = helper(root)
        return result
