_author_ = 'jake'
_project_ = 'leetcode'












class Solution(object):
    def numSubarrayBoundedMax(self, A, L, R):
        """
        :type A: List[int]
        :type L: int
        :type R: int
        :rtype: int
        """
        subarrays, total = 0, 0
        last_above_max = -1
        for i, num in enumerate(A):
            if num > R:
                subarrays = 0
                last_above_max = i
            elif num < L:
                total += subarrays
            else:
                subarrays = i - last_above_max
                total += subarrays
        return total
