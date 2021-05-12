from collections import defaultdict


class Solution(object):
    def maxLevelSum(self, root):
        level_sums = defaultdict(int)

        def helper(node, level):
            if not node:
                return
            level_sums[level] += node.val
            helper(node.left, level + 1)
            helper(node.right, level + 1)
        helper(root, 1)
        max_level_sum = max(level_sums.values())
        return min(level for level, level_sum in level_sums.items() if level_sum == max_level_sum)
