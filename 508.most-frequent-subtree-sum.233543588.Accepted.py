







from collections import defaultdict


class Solution(object):
    def findFrequentTreeSum(self, root):

        def count_sums(node):
            if not node:
                return 0
            total_sum = node.val + count_sums(node.left) + count_sums(node.right)
            tree_sums[total_sum] += 1
            return total_sum
        if not root:
            return []
        tree_sums = defaultdict(int)
        count_sums(root)
        max_sum = max(tree_sums.values())
        result = []
        for key, val in tree_sums.items():
            if val == max_sum:
                result.append(key)
        return result
