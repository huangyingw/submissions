_author_ = 'jake'
_project_ = 'leetcode'










from collections import namedtuple


class Solution(object):
    def subtreeWithAllDeepest(self, root):

        Result = namedtuple("Result", ["node", "depth"])

        def helper(node):
            if not node:
                return Result(None, -1)
            left_result, right_result = helper(node.left), helper(node.right)
            depth_diff = left_result.depth - right_result.depth
            if depth_diff == 0:
                return Result(node, left_result.depth + 1)
            if depth_diff > 0:
                return Result(left_result.node, left_result.depth + 1)
            return Result(right_result.node, right_result.depth + 1)
        return helper(root).node
