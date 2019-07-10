_author_ = 'jake'
_project_ = 'leetcode'








from collections import defaultdict


class Solution:
    def subarraysDivByK(self, A, K):

        result = 0
        running_sum = 0
        prefix_sums = defaultdict(int)
        prefix_sums[0] = 1
        for num in A:
            running_sum = (running_sum + num) % K
            result += prefix_sums[running_sum]
            prefix_sums[running_sum] += 1
        return result
