_author_ = 'jake'
_project_ = 'leetcode'












from collections import defaultdict


class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        x_to_y_and_val = defaultdict(list)

        def helper(node, x, y):
            if not node:
                return
            x_to_y_and_val[x].append((-y, node.val))
            helper(node.left, x - 1, y - 1)
            helper(node.right, x + 1, y - 1)
        helper(root, 0, 0)
        result = []
        xs = sorted(x_to_y_and_val.keys())
        for x in xs:
            x_to_y_and_val[x].sort()
            result.append([val for _, val in x_to_y_and_val[x]])
        return result
