class Solution(object):
    def maximumSum(self, arr):
        if all(a <= 0 for a in arr):
            return max(arr)
        overall_max_deleted = 0
        max_here, max_here_deleted = 0, 0
        for a in arr:
            max_here_deleted = max(max_here_deleted + a, max_here)
            max_here = max(max_here, 0) + a
            overall_max_deleted = max(overall_max_deleted, max_here_deleted, max_here)
        return overall_max_deleted
