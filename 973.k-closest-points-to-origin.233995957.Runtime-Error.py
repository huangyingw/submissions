_author_ = 'jake'
_project_ = 'leetcode'







import heapq


class Solution:
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        return heapq.nsmallest(K, points, lambda x, y: x * x + y * y)
