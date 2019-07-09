_author_ = 'jake'
_project_ = 'leetcode'














class Solution(object):
    def maxSubarraySumCircular(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if all(num <= 0 for num in A):
            return max(A)
        overall_max, overall_min = float('-inf'), float('inf')
        max_ending_here, min_ending_here = 0, 0
        for num in A:
            max_ending_here = max(max_ending_here, 0) + num
            min_ending_here = min(min_ending_here, 0) + num
            overall_max = max(overall_max, max_ending_here)
            overall_min = min(overall_min, min_ending_here)
        return max(overall_max, sum(A) - overall_min)
