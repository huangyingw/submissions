









from collections import Counter


class Solution(object):
    def numFactoredBinaryTrees(self, A):

        MOD = 10 ** 9 + 7
        num_to_trees = Counter(A)
        A.sort()
        for i, num in enumerate(A):
            for left in A[:i]:
                right, remainder = divmod(num, left)
                if right <= 1:
                    break
                if remainder == 0 and right in num_to_trees:
                    num_to_trees[num] += num_to_trees[left] * num_to_trees[right]
        return sum(num_to_trees.values()) % MOD
