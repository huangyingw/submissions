from collections import defaultdict


class Solution:
    def numSubarraysWithSum(self, A, S):
        result = 0
        running = 0
        partials = defaultdict(int, {0: 1})
        for i, a in enumerate(A):
            running += a
            result += partials[running - S]
            partials[running] += 1
        return result
